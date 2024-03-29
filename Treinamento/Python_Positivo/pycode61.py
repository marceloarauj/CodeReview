# Roberto Ritter de Oliveira Filho
# 30/11/2005
# Curitiba - Brasil
# Prolog em Python
#
#

global ListaHomem #cria a ListaHomem global
global ListaMulher #cria a ListaMulher global
global ListaProgenitor #cria a ListaProgenitor global
global ListaFuncoes #cria a ListaFuncoes global
ListaProgenitor={} #inicia dicionario ListaProgenitor
ListaFuncoes={'pai': 'func_pais(x,y,"homem")', \
              'mae': 'func_pais(x,y,"mulher")',\
              'filho':'func_filhos(x,y,"homem")',\
              'filha':'func_filhos(x,y,"mulher")',\
              'avoh':'func_avos(x,y,"homem")',\
              'avom':'func_avos(x,y,"mulher")',\
              'irmao':'func_irmaos(x,y,"homem")',\
              'irma':'func_irmaos(x,y,"mulher")',\
              'tio':'func_tios(x,y,"homem")',\
              'tia':'func_tios(x,y,"mulher")',\
              'sobrinho':'func_sobrinhos(x,y,"homem")',\
              'sobrinha':'func_sobrinhos(x,y,"mulher")',\
              'marido':'func_casal(x,y,"homem")',\
              'esposa':'func_casal(x,y,"mulher")'} #inicia dicionario ListaFuncoes
ListaHomem=[] #inicia lista ListaHomem
ListaMulher=[] #inicia lista ListaMulher

def func_existe(nomedoarquivo):# funcao verifica se o arquivo existe
    try:
        global arquivolido
        arquivo = open(nomedoarquivo,"r")
        arquivolido=arquivo.readlines() #separa as linhas do arquivo
        func_mensagem("PRO",nomedoarquivo)
        return arquivolido
    except:
        func_mensagem('ER',nomedoarquivo)

def func_arquivo():# funcao do arquivo a ser lido
    nomedoarquivo=raw_input("Digite o nome do Arquivo: ")
    arquivolido=func_existe(nomedoarquivo)
    if(arquivolido!=None):
        func_estruturadosfatos() #inicia a leitura do arquivo e montagem dos fatos
        func_prolog(arquivolido) #inicia o prolog com o arquivo lido como parâmetro

def func_mensagem(msn,oq): #retorno de mensagens do arquivo
    if(msn=='ER'):
        print "Erro! Arquivo '"+oq+"' não existe! "
        sair=raw_input("'s' para sair e qualquer tecla para continuar: ")
        if (sair.lower()!='s'):
            func_arquivo()
    if(msn=='PRO'):
        print "Processando..."+oq
        print ""
    if(msn=='OK'):
        print "Pronto!"+oq

def func_prolog(arquivolido): #funcao prolog
    raw_input()
    print """
        ===================================
        Consultas Disponiveis:
        -----------------------------------
        marido(marido,y).
        esposa(esposa,y).
        irmao(irma(o),irmao).
        irma(irma(o),irma).
        pai(pai,filho).
        pai(x,y).
        mae(mae,filho).
        mae(x,y).
        filho(filho,pai/mae).
        filha(filha,pai/mae).
        avoh(avohomem,neto(a)).
        avom(avomulher,neto(a).
        tio(tio,sobrinho(a)).
        tia(tia,sobrinho(a).
        sobrinho(sobrinho,tio(a)).
        sobrinha(sobrinha,tio(a)).
        homem(x).
        mulher(x).
        ====================================
    """
    pergunta=raw_input("Pergunta ('s' para sair) ?:- ")
    if str(pergunta.lower())!='s': #verifica se a pergunta e <> de s e inicia o bloco abaixo
        if ((pergunta.count("(")==1) and (pergunta.count(";")==1 or pergunta.count(".")==1) and (pergunta.count(")")==1)):
            #a linha acima verifica se a pergunta esta no formato correto. eg. ().
            # testa para ver se a pergunta esta montada corretamente
            consulta=pergunta.split('(')[0] #retorna o primeiro elemento homem no caso de homem(x).
            variavelx=pergunta.split('(')[1].split(')')[0] #retorna o elemento entre os ()
            #pega o elemento x na pergunta homem(x).
            if (variavelx=="x" and consulta=="homem"): #se for == x homem retornara a Lista de Homens. eg. homem(x).
                print "\n".join(ListaHomem)
                func_prolog(arquivolido)
            if (variavelx=="x" and consulta=="mulher"): #se for == x e mulher retornara a Lista de Mulheres. eg. mulher(x).
                print "\n".join(ListaMulher)
                func_prolog(arquivolido)
            if (variavelx!="x" and consulta in ListaFuncoes): #se for <> x e estiver no dicionario ListaFuncoes executa
                y,x=func_separa(pergunta) #separa os valores de x,y na pergunta nonono(x,y). e retorna em filho e progenitor
                eval(ListaFuncoes[consulta]) #executa funcao q esta no dicionario, com base na pergunta feita
            else:
                print "Pergunta não funciona!"
        else:
            print ("Falta colocar '.' ou '(' ou ')' ou ';' ")
            func_prolog(arquivolido)

def func_separa(pergunta): #funcao para separar x e y
    filho=pergunta.split("(")[1].split(")")[0].split(",")[1] #pega o elemento x de x,y
    progenitor=pergunta.split("(")[1].split(")")[0].split(",")[0] #pega o elemento y de x,y
    return filho,progenitor #retorna para a funcao

def func_sobrinhos(x,y,tipo):   #verifica SOBRINHO ou SOBRINHA e TIO ou TIA e sobrinho e o tipo e do dicionario
    Listas=func_listas(tipo) #chama funcao q retornara lista homem ou mulher
    achei=0
    if ((x in Listas)):
        for i in range(len(ListaProgenitor)):
                tmp2=ListaProgenitor.keys()[i]
                if x in ListaProgenitor[tmp2]:
                    #print tmp2
                    paidosobrinho=tmp2
        for i in range(len(ListaProgenitor)):
                tmp=ListaProgenitor.keys()[i]
                if ((y in ListaProgenitor[tmp]) and (paidosobrinho in ListaProgenitor[tmp]) and (paidosobrinho != y)):
                    achei=1
    if(achei==1):
        func_prolog_msg(True)
    else:
        func_prolog_msg(False)

def func_casal(x,y,tipo):
    Listas=func_listas(tipo)
    if x in Listas:
        if (x in ListaProgenitor):
            filho=ListaProgenitor[x]
            for j in range(len(ListaProgenitor)):
                if ((x != ListaProgenitor.keys()[j])):
                    if (filho == ListaProgenitor[ListaProgenitor.keys()[j]]):
                        y=ListaProgenitor.keys()[j]
                        print "Casal: "+x+" "+y
                        func_prolog_msg(True)

        else:
            func_prolog_msg(False)

    else:
        func_prolog_msg(False)




def func_tios(x,y,tipo):   #verifica TIO ou TIA e sobrinho e o tipo e do dicionario
    Listas=func_listas(tipo)#chama funcao q retornara lista homem ou mulher
    achei=0
    if ((x in Listas)):
        for i in range(len(ListaProgenitor)):
                tmp2=ListaProgenitor.keys()[i]
                if y in ListaProgenitor[tmp2]:
                    #print tmp2
                    paidosobrinho=tmp2
        for i in range(len(ListaProgenitor)):
                tmp=ListaProgenitor.keys()[i]
                if ((x in ListaProgenitor[tmp]) and (paidosobrinho in ListaProgenitor[tmp]) and (paidosobrinho != x)):
                    achei=1
    if(achei==1):
        func_prolog_msg(True)
    else:
        func_prolog_msg(False)

def func_avos(z,x,tipo): #verifica AVOH ou AVOM e netos e o tipo e do dicionario
    Listas=func_listas(tipo)#chama funcao q retornara lista homem ou mulher
    if ((z in Listas) and (z in ListaProgenitor)):
        for i in range(len(ListaProgenitor[z])):
            if ListaProgenitor[z][i] in ListaProgenitor:
                if x in ListaProgenitor[ListaProgenitor[z][i]]:
                    func_prolog_msg(True)
                else:
                    func_prolog_msg(False)
    else:
        func_prolog_msg(False)

def func_irmaos(x,y,tipo):#verifica IRMAO ou IRMA, irmaos ou  e o tipo e do dicionario
    Listas=func_listas(tipo)#chama funcao q retornara lista homem ou mulher
    if ((y in Listas)):
        for i in range(len(ListaProgenitor)):
            tmp=ListaProgenitor.keys()[i]
            if x in ListaProgenitor[tmp] and y in ListaProgenitor[tmp]:
                func_prolog_msg(True)
            else:
                None

    else:
        func_prolog_msg(False)

def func_filhos(x,y,tipo): #verifica FILHO ou FILHA e pai ou mae e o tipo e do dicionario
    Listas=func_listas(tipo)#chama funcao q retornara lista homem ou mulher
    if ((x in Listas) and (y in ListaProgenitor)):
        if x in ListaProgenitor[y]:
            func_prolog_msg(True)
        else:
            func_prolog_msg(False)
    else:
        func_prolog_msg(False)

def func_pais(x,y,tipo): #verifica PAI ou MAE e filhos
    Listas=func_listas(tipo)#chama funcao q retornara lista homem ou mulher
    if ((x!='x')and (y!='y')):
        if ((x in Listas) and (x in ListaProgenitor)):
            if y in ListaProgenitor[x]:
                func_prolog_msg(True)
            else:
                func_prolog_msg(False)
    elif ((x=='x') and (y=='y')):
        for i in ListaProgenitor:
            if i in Listas:
                print 'Pai ou Mãe : '+i
                for j in ListaProgenitor[i]:
                    print 'Filho(a) : '+j
        func_prolog_msg(True)
    elif ((x!='x') and (y=='y')):
        if ((x in Listas) and (x in ListaProgenitor)):
            print 'Pai ou Mãe: '+x
            for j in ListaProgenitor[x]:
                print 'Filho(a) : '+j
            func_prolog_msg(True)
        else:
            func_prolog_msg(False)

    else:
        func_prolog_msg(False)

def func_listas(tipo): #le do dicionario o parametro tipo e retorna lista correta
    Listas=[]
    if (tipo=='homem'):
        Listas=ListaHomem
    else:
        Listas=ListaMulher
    return Listas

def func_estruturadosfatos(): #monta as Listas Homem e Mulher e o Dicionario ListaProgenitor
    for i in range(len(arquivolido)):
        if len(arquivolido[i])>4:
            verifica=arquivolido[i].split('(')[0]
            variavelx=arquivolido[i].split("(")[1].split(")")[0]
            if (verifica=="homem"):
                ListaHomem.append(variavelx)
            if (verifica=="mulher"):
                ListaMulher.append(variavelx)
            if (verifica=="progenitor"):
                filho=arquivolido[i].split("(")[1].split(")")[0].split(",")[1]
                pai=arquivolido[i].split("(")[1].split(")")[0].split(",")[0]
                if pai in ListaProgenitor:
                    ListaProgenitor[pai].append(filho)
                else:
                    ListaProgenitor[pai]=[filho]

def func_prolog_msg(msg): #retorna mensagens do prolog
    if msg==True:
        print "Sim"
    if msg==False:
        print "Nao"
    func_prolog(arquivolido)

def main():
    print "=======PROLOG EM PYTHON======="
    func_arquivo()

if __name__ == "__main__":
    main()