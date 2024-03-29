#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import select
import socket
import itertools

# Algumas constantes usadas

INPUT_READ = 0
INPUT_WRITE = 1
INPUT_EXCEPTION = 2

_read  = {}
_write = {}
_error = {}

_modes = [_read, _write, _error]
_select = select.select

_tags = itertools.count()

class _Wrapper(object):
    # Classe wrapper para os sockets ou arquivos usados
    
    def __init__(self, source, callback):
        self.source = source
        self.fileno = source.fileno
        self.close = source.close
        self.callback = callback


class TkSelectMixIn:
    # Classe wrapper para select.select().

    def input_add(self, source, mode, callback):
        # Insere um objeto na pilha e retorna um identificador
        #
        # source é o objeto, normalmente um socket
        #
        # mode é uma das constantes INPUT_READ, INPUT_WRITE ou
        # INPUT_EXCEPTION
        #
        # callback é o método a ser chamado quando a condição
        # monitorada for satisfeita

        if mode not in (0, 1, 2):
            raise ValueError("modo inválido")

        tag = _tags.next()
        _modes[mode][tag] = _Wrapper(source, callback)

        return tag

    def input_remove(self, tag):
        # Remove um objeto da pilha. key é o identificador retornado
        # quando o objeto foi inserido
        # Note que o socket NÃO É FECHADO, apenas removido
        
        for mode in _modes:
            if tag in mode:
                mode.pop(tag)
                break

    def _check(self):
        # Verifica todos os sockets sendo usados e remove quaisquer
        # que estejam com problemas
        
        for mode in _modes:
            for tag, source in mode.iteritems():
                try:
                    _select([source], [source], [source], 0)
                except: # encontramos o vilão
                    mode.remove(tag)
                    source.close()
        
    def _select(self,
              # Essa declaração estranha tem uma finalidade. Armazenar
              # as globais no namespace local, acelerando a consulta
              # de nomes, permitindo que este método seja executado o
              # mais rápido possível.
              _read=_read,
              _write=_write,
              _error=_error,
              _select=_select):


        while 1:

            # tentamos o select até não ocorrer erros
            try:
                ready = _select(_read.values(), _write.values(),
                                _error.values(), 0)
                break
            except ValueError:
                # Um socket inválido foi passado... 
                self._check()
            except TypeError:
                # Algo que não era um socket foi passado...
                self._check()
            except socket.error, reason:
                # Algum dos sockets está com problemas... 
                code, msg = reason.args
                if code == EINTR:
                    # consulte man 2 select
                    return
                if code == EBADF:
                    # Socket com problemas... 
                    self._check()
                else:
                    # Se chegamos aqui, realmente não sei o que ocorreu
                    raise

        for condition, mode in enumerate(ready):
            for source in mode:
                source.callback(source.source, condition)

        self.after(100, self._select)
        

    def start(self):
        self.after(100, self._select)



if __name__ == '__main__':

    import Tkinter
    from ScrolledText import ScrolledText
    from Tkconstants import *

    class MainWindow(Tkinter.Tk, TkSelectMixIn):
        def __init__(self):
            Tkinter.Tk.__init__(self)
            
            self.textbox = ScrolledText(self, bg='white')
            self.textbox.pack(fill=BOTH, expand=1)
            self.server()
            self.start()

        def server(self):
            # inicializa o servidor

            self.sock = socket.socket(socket.AF_INET, \
                                      socket.SOCK_STREAM)
            self.sock.bind(('localhost', 8000))
            self.sock.listen(1)

            # a chamada para input_read para o socket do servidor é
            # um pouco diferente, tendo como callback o método
            # self.accept
            self.server_tag = self.input_add(self.sock, \
                                             INPUT_READ, self.accept)
            # mantemos uma lista dos clientes conectados
            self.clients = {}

        def accept(self, source, condition):
            # método chamado quando o servidor tem um cliente
            # esperando para ser aceito

            conn, addr = source.accept()
            self.insert("%s:%s conectado\n" % addr)

            # insere o cliente na lista e registra o método self.write
            # como callback para quando existirem dados esperando para
            # serem lidos.

            self.clients[addr] = (conn, self.input_add(conn,
                                               INPUT_READ, self.write))
        def write(self, source, condition):
            # método chamado quando um cliente envia dados

            data = source.recv(1024)
            if not data.strip() or data.strip() == 'bye':
                # se o cliente enviar um "bye" ou uma linha em branco,
                # desconecte-o
                source.close()

                for addr, (conn, tag) in self.clients.iteritems():
                    if source is conn:
                        self.input_remove(tag)
                        self.insert('%s:%s desconectado\n' % addr)
                        del self.clients[addr]
                        break
            else:
                for (addr, port), (conn, tag) in \
                   self.clients.iteritems():
                    if source is conn:
                        self.insert('%s:%s>>>%s\n'%(addr, port, \
                                    data.strip()))
                        break

        def insert(self, data):
            self.textbox.insert(END, data)
            self.textbox.see(END)

        def quit(self):
            self.input_remove(self.server_tag)
            for add, (conn, tag) in self.clients.iteritems():
                self.input_remove(tag)
                conn.close()
            self.sock.close()
            Tkinter.Tk.destroy(self)

if __name__ == "__main__":
    root = MainWindow()
    Tkinter.mainloop()