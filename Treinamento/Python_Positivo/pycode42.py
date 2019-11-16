#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-


from inscritos import inscritos

from Tkinter import *
from Dialog import Dialog
import time
import random

class MainFrame(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.master.title("Sorteia")
        self.text = StringVar()
        self.nome = StringVar()
        self.createWidgets()
        self.pack(padx=10, pady=10)


    def createWidgets(self):
        panel1 = Frame(self)
        nomeL = Label(panel1, text="Nome:")
        nomeL.pack(side=LEFT)
        self.nomeE = Entry(panel1, \
            textvariable=self.nome, width=50)
        self.nomeE.pack(side=LEFT)
        self.nomeE.bind("<Return>", self.addEnter)
        addB = Button(panel1, text="  +  ", \
                      command=self.adicionar)
        addB.pack(side=LEFT)
        subB = Button(panel1, text="  -  ", \
                      command=self.remover)
        subB.pack(side=LEFT)
        panel1.pack(side=TOP)

        panel2 = Frame(self)

        scrollbar = Scrollbar(panel2, orient=VERTICAL)
        self.listbox = Listbox(panel2, \
                       yscrollcommand=scrollbar.set, \
                       font=("Tahoma", 10, "bold"))
        self.listbox.pack(side=LEFT, fill=BOTH, expand=1)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        panel2.pack(side=TOP, fill=BOTH, \
                              expand=Y, pady=10)

        panel3 = Frame(self)

        sorteiaB = Button(panel3, text="Sorteia",\
                          font=("Tahoma", 10, "bold"), \
                          command=self.sorteia)

        sorteiaB.pack(side=TOP, fill=BOTH, expand=Y)

        nomeSorteadoT = Label(panel3, \
                             textvariable=self.text, \
                             font=("Tahoma", 20, "bold"))
        nomeSorteadoT.pack(side=TOP, fill=BOTH, \
                             expand=Y, pady=20)

        self.nomeSorteadoT = nomeSorteadoT

        panel3.pack(side=TOP, fill=BOTH, expand=Y)
        random.shuffle(inscritos)
        for nome in inscritos:
                self.listbox.insert(END, nome)


    def sorteia(self):
        listaSorteia = self._getLista()
        random.shuffle(listaSorteia)
        self.nomeSorteadoT['fg'] = 'black'
        if not listaSorteia:
            return

        t = 0

        while len(listaSorteia) > 1:
            nome = random.choice(listaSorteia)
            self.after(t, self.text.set, nome)
            t += 1000 / len(listaSorteia)
            listaSorteia.remove(nome)

        sorteado = listaSorteia.pop()
        self.after(t, self.fimSorteio, sorteado)

    def fimSorteio(self, sorteado):
        self.text.set(sorteado)
        self.nomeSorteadoT['fg'] = 'red'
        self.bell()

    def _getLista(self):
        listbox = self.listbox

        lista = [listbox.get(i) for i in range(listbox.size())]
        return lista

    def adicionar(self):
        nome = self.nome.get()
        if not len(nome):
            Dialog(self, title="Erro!", \
                         text="Nome inválido", \
                         bitmap='error', \
                         default=0, \
                         strings=('OK',))
            return

        if nome in self._getLista():
            Dialog(self, title="Erro!", \
                         text="Já cadastrado", \
                         bitmap='error', \
                         default=0, \
                         strings=('OK',))
            return

        self.listbox.insert(END, nome)
        self.limpaCampos()

    def addEnter(self, ev):
        self.adicionar()

    def remover(self):
        self.listbox.delete(ANCHOR)

    def limpaCampos(self):
        self.nome.set("")
        self.nomeE.focus()



def main():
    frm = MainFrame()
    frm.mainloop()

if __name__ == '__main__':
    main()