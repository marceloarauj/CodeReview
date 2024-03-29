#!/usr/bin/env python
# -*- coding:UTF-8 -*-

import socket
import gtk
import GDK

class MainWindow(gtk.GtkWindow):
    def __init__(self):
        gtk.GtkWindow.__init__(self, gtk.WINDOW_TOPLEVEL)
        self.connect("destroy", self.quit)
        self.connect("delete_event", self.quit)
        self.show()
    
        self.set_usize(500, 210)
        self.main_box = gtk.GtkVBox(False, 1)
        self.main_box.set_border_width(1)
        self.add(self.main_box)
        self.body()
        self.server()
        self.main_box.show()

    def body(self):
        textbox = self.textbox = gtk.GtkText()
        textbox.set_editable(True)
        self.main_box.pack_start(textbox, True, True, 0)
        textbox.show()

        entry = self.entry = gtk.GtkEntry(1024)
        self.main_box.pack_start(entry, True, True, 0)
        entry.show()

        send = gtk.GtkButton('Enviar')
        send.connect('clicked', self.send)
        self.main_box.pack_start(send, True, True, 0)
        send.show()

    def send(self, data=None, widget=None):
        text = self.entry.get_text()
        self.do_send(text)
        self.entry.set_text('')

        # nada de novo até aqui

    def do_send(self, data):

        # envia ''data'' para todos os clientes conectados

        for addr, (conn, tag) in self.clients.iteritems():
            conn.send(data)

    def server(self):

        # inicializa o servidor

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('localhost', 8000))
        self.sock.listen(1)

        # a chamada para input_read para o socket do servidor é um pouco 
        # diferente, tendo como callback o método self.accept

        self.server_tag = gtk.input_add(self.sock, GDK.INPUT_READ, \
                                          self.accept)

        # mantemos uma lista dos clientes conectados

        self.clients = {}

    def accept(self, source, condition):

        # método chamado quando o servidor tem um cliente 
        # esperando para ser aceito

        conn, addr = source.accept()
        self.insert("%s:%s conectado\n" % addr)

        # insere o cliente na lista e registra o método self.write
        # como  callback para quando existirem dados esperando
        # para serem lidos

        self.clients[addr] = (conn, gtk.input_add(conn, \
                               GDK.INPUT_READ, self.write))

    def write(self, source, condition):

        # método chamado quando um cliente envia dados 

        data = source.recv(1024)
        if data.strip() == 'bye' or not len(data):

            # se o cliente enviar um ''bye'', desconecte-o :)

            source.close()
            for addr, (conn, tag) in self.clients.iteritems():
                if source is conn:
                    gtk.input_remove(tag)
                    self.insert('%s:%s desconectado\n' % addr)
                    del self.clients[addr]
                    break
        else:
            for (addr, port), (conn, tag) in self.clients.iteritems():
                if source is conn:
                    self.insert('%s:%s >>> %s\n'%(addr, port, \
                                data.strip()))
                    break

    def insert(self, data):
        self.textbox.insert_defaults(data)

    def quit(self, *args):
        gtk.input_remove(self.server_tag)
        for addr, (conn, tag) in self.clients.iteritems():
            gtk.input_remove(tag)
            conn.close()
        self.sock.close()

        self.hide()
        self.destroy()
        gtk.mainquit()

if __name__ == '__main__':
    MainWindow()
    gtk.mainloop()