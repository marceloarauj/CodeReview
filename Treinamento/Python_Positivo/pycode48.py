#!/usr/bin/env python
import Tkinter, sys
class window:
        def __init__(self): #constructor
                self.window = Tkinter.Tk()
                self.window.title("APM Monitor")
                self.frame  = Tkinter.Frame(self.window)
                self.label  = Tkinter.Label(self.frame)
                self.button = Tkinter.Button(self.frame, text="Exit", command=sys.exit)

        def read_apm(self): #le o arquivo /proc/apm onde ficam as informacoes
                apm = file('/proc/apm').readline().split(' ') # da um split junto da leitura
                return( { 'ac': apm[3], 'charge': apm[6] } )  # retorna um dicionario com as informacoes

        def set_params(self):
                params = self.read_apm()
                ac = params['ac']
                charge = params['charge'] # guarda o valor da carga da bateria
                if ac == "0x01" : ac = "on-line"  # verifica a bateria e diz se esta on-line
                else: ac = "off-line"             # off-line (ninguem ia querer ver 0x01 ou 0x00 :)
                self.label.configure(text="AC: " + ac + " | Charge: " + charge)

        def loop_apm(self):
                self.set_params()
                self.window.after(2000, self.loop_apm) #esta parte eu gostei, ele agenda a execucao
                                                       # dele mesmo para daqui 2 segundos :)

        def packs(self):
                self.label.pack()
                self.button.pack()     # packeia tudo :)
                self.frame.pack(expand="true")

if __name__=="__main__":
         monitor = window()
         monitor.packs()
         monitor.loop_apm()
         monitor.frame.mainloop()