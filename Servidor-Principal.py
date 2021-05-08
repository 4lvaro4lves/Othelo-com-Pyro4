import Pyro4
import time
import threading
from tkinter import *
Tempo=time.time()
print ("\n\n-------------->>  SERVIDOR  <<--------------\n\n")
##############################################################################################################################
#configuração servidor
@Pyro4.expose
class Botao:
    def bt01 (self):
        print ("--------------------> Dentro do Botao 01")
        bt81 = Button(janelaPrincipal,width=5,height=3,bg='black',command=threading.Thread(target=(retornobt02))).place(x=0, y=0)
        return (retornobt01())
    def bt02 (self):
        print ("--------------------> Dentro do Botao 02")
        return (retornobt02())

daemon = Pyro4.Daemon()
uri = daemon.register(Botao)
ns = Pyro4.locateNS()
ns.register('Botao', uri)
print (uri)
comunicar = threading.Thread(target=daemon.requestLoop)

##############################################################################################################################
#Botões
def retornobt01():
    print ("--------------------> Função Retorno bt01.")
    return ('bt01')
def retornobt02():
    print ("--------------------> Função Retorno bt02.")
    return ('bt02')
##############################################################################################################################
#configuração jogo
janelaPrincipal = Tk()
janelaPrincipal.geometry("650x450")
janelaPrincipal.resizable(width=0, height=0)
janelaPrincipal.title("Jogo Othello(Reversi) com Pyro4 - SERVIDOR")
#nome=input("Digite seu nome: ")
imagemVerde = PhotoImage(file="imagemVerde.png")
imagemVermelha = PhotoImage(file="imagemVermelha.png")
imagemReferencia=64*[0]

global contVerde, contVermelho
contVerde = 0
contVermelho = 0
msgTela = ''

##############################################################################################################################
#main


def tempo():
    while (True):
        print (time.time())
        time.sleep(1)
    
print ('main')
def main():
    comunicar.start.mainloop()#daemon.requestLoop().mainloop()
    print ("FIM main")

main()
print ("Final de Tudo.")
tempoAtual = threading.Thread(target=tempo)

tempoAtual.start()
##############################################################################################################################



