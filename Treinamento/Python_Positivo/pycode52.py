import socket
import sys

class LenghtError(Exception):
    pass
class RepeatedDigitsError(Exception):
    pass

def testNum(num): 
"""Funcao para testar se o número possui digitos repetidos ou
se é maior que 4."""
    if len(num) != 4:
        raise LenghtError 
    for i in num:
        if num.count(i) > 1: raise RepeatedDigitsError
        
class GameCon:
    """Classe para cuidar da conexao do jogo"""
    def __init__(self):
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def con(self, ip, port=1911):
        self.sock.connect((ip, port))

    def waitCon(self, ip='', port=1911, l=1):
        self.sock.bind((ip, port))
        self.sock.listen(l) 
        (clientsocket, address) = self.sock.accept()
        self.sock = clientsocket 
    
    def send(self, msg):
        sent = self.sock.send(msg)
        if sent == 0:
            raise BrokenCon, "socket connection broken"

    def receive(self, bytes):
        return self.sock.recv(bytes)

    def close(self):
        self.sock.close()


class Senha: 
    """Classe do jogo senha"""
    def __init__(self, myNum, hisNum):
        self.myNum  = str(myNum)  #Numero do cliente
        self.hisNum = str(hisNum) #Numero do server(adversario)

    def check(self, checkNum):
    """Metodo para checar o numero de bombas e tiros de um determinado
numero em relacao ao self.hisNum(numero do adversrio)"""
        total    = 0  #Total de numeros coicidentes
        bombs    = 0
        for a in checkNum:
            total+=self.hisNum.count(a)
            
        for i in xrange(4):
            if checkNum[i] == self.hisNum[i]: bombs+=1

        shots = total - bombs
        return bombs, shots

   
def sender(skt, pwd):
"""Funcao que recebe o numero a ser testado e o envia para o
adversario e verifica vitoria"""
    while True:
        try:
            num = raw_input('Digite o numero a ser testado: ').strip()
            testNum(num)
            skt.send(num)
            break
        except LenghtError:
            print '!!\nO numero deve ter quatro digitos\n...'
        except RepeatedDigitsError:
            print '!!\nO numero nao pode ter digitos repetidos\n...'
        
       
    print 'Bombas: %s Tiros: %s' % pwd.check(num)
    if num == pwd.hisNum: # Se o numero que testei eh igual do
                          # adversario, eu ganho
        print '\n\nVOCE GANHOU! Parabens :-)'
        skt.close()
        if raw_input('Jogar denovo? [s/n] ').startswith('s'):
            main()
        else: sys.exit()
    getter(skt, pwd) # Um metodo que chama o outro num loop
                     # continuo, deve ser a pior solucao para
                     # meu problema :-/

def getter(skt, pwd):      
"""Funcao que recebe o numero tentado pelo adversrio, o imprime
na tela e verifica derrota"""
    print '\nEsperando a escolha do adversario...'
    hisNum = skt.receive(4)
    print '::Ele chutou: %s\n' % hisNum
    if hisNum == pwd.myNum:
        print '\n\nVOCE PERDEU! :-('
        skt.close()
        if raw_input('Jogar denovo? [s/n] ').startswith('s'):
            main()
        else: sys.exit()
    sender(skt, pwd)

def main():
    talker = GameCon()           #Cria um objeto socket
    while True:
        print '1. Servidor\n2. Cliente'
        choice = input('Escolha: ')
        if choice == 1 or choice == 2: break

    if choice == 1:
        print 'Esperando conexao...'
        talker.waitCon()
            
    else:
        while True:
            ip = raw_input('Digite o IP do servidor: ').strip()
            try:
                talker.con(ip)
                break
            except: print 'Conexao nao aceita'
    
    while True:
        try:
            myNum = raw_input('Digite seu numero: ').strip()
            testNum(myNum)
            talker.send(myNum)
            hisNum = talker.receive(4)
            game = Senha(myNum, hisNum)
            break
        except LenghtError:
            print '!!\nO numero deve ter quatro digitos\n...'
        except RepeatedDigitsError:
            print '!!\nO numero nao pode ter digitos repetidos\n...'


    if choice == 1:
       sender(talker, game)
    else:
       getter(talker, game)

if __name__ == '__main__':
    main()