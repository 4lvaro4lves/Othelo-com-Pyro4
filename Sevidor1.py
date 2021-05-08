import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip
import threading
import Pyro4
print ('Servidor')


def imprimir(arg):
    print ('Função imprimir')
    print ('Função imprimir')
    
def mudar():
    j.botao82.setStyleSheet('QPushButton{background-color:#000000}')

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo     = 100
        self.esquerda = 100
        self.largura  = 800
        self.altura   = 600
        self.titulo   = 'Primeira'
#linha01
        self.botao11 = QPushButton(self)
        self.botao11.move(0,350)
        self.botao11.resize(50,50)
        self.botao11.setStyleSheet('QPushButton{background-color:#ffffff}')
        self.botao11.clicked.connect(self.bt11)

        self.botao12 = QPushButton(self)
        self.botao12.move(50,350)
        self.botao12.resize(50,50)
        self.botao12.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao13 = QPushButton(self)
        self.botao13.move(100,350)
        self.botao13.resize(50,50)
        self.botao13.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao14 = QPushButton(self)
        self.botao14.move(150,350)
        self.botao14.resize(50,50)
        self.botao14.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao15 = QPushButton(self)
        self.botao15.move(200,350)
        self.botao15.resize(50,50)
        self.botao15.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao16 = QPushButton(self)
        self.botao16.move(250,350)
        self.botao16.resize(50,50)
        self.botao16.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao17 = QPushButton(self)
        self.botao17.move(300,350)
        self.botao17.resize(50,50)
        self.botao17.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao18 = QPushButton(self)
        self.botao18.move(350,350)
        self.botao18.resize(50,50)
        self.botao18.setStyleSheet('QPushButton{background-color:#000000}')
#linha02     
        self.botao21 = QPushButton(self)
        self.botao21.move(0,300)
        self.botao21.resize(50,50)
        self.botao21.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao22 = QPushButton(self)
        self.botao22.move(50,300)
        self.botao22.resize(50,50)
        self.botao22.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao23 = QPushButton(self)
        self.botao23.move(100,300)
        self.botao23.resize(50,50)
        self.botao23.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao24 = QPushButton(self)
        self.botao24.move(150,300)
        self.botao24.resize(50,50)
        self.botao24.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao25 = QPushButton(self)
        self.botao25.move(200,300)
        self.botao25.resize(50,50)
        self.botao25.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao26 = QPushButton(self)
        self.botao26.move(250,300)
        self.botao26.resize(50,50)
        self.botao26.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao27 = QPushButton(self)
        self.botao27.move(300,300)
        self.botao27.resize(50,50)
        self.botao27.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao28 = QPushButton(self)
        self.botao28.move(350,300)
        self.botao28.resize(50,50)
        self.botao28.setStyleSheet('QPushButton{background-color:#ffffff}')
#linha03
        self.botao31 = QPushButton(self)
        self.botao31.move(0,250)
        self.botao31.resize(50,50)
        self.botao31.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao32 = QPushButton(self)
        self.botao32.move(50,250)
        self.botao32.resize(50,50)
        self.botao32.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao33 = QPushButton(self)
        self.botao33.move(100,250)
        self.botao33.resize(50,50)
        self.botao33.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao34 = QPushButton(self)
        self.botao34.move(150,250)
        self.botao34.resize(50,50)
        self.botao34.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao35 = QPushButton(self)
        self.botao35.move(200,250)
        self.botao35.resize(50,50)
        self.botao35.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao36 = QPushButton(self)
        self.botao36.move(250,250)
        self.botao36.resize(50,50)
        self.botao36.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao37 = QPushButton(self)
        self.botao37.move(300,250)
        self.botao37.resize(50,50)
        self.botao37.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao38 = QPushButton(self)
        self.botao38.move(350,250)
        self.botao38.resize(50,50)
        self.botao38.setStyleSheet('QPushButton{background-color:#000000}')
#linha04        
        self.botao41 = QPushButton(self)
        self.botao41.move(0,200)
        self.botao41.resize(50,50)
        self.botao41.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao42 = QPushButton(self)
        self.botao42.move(50,200)
        self.botao42.resize(50,50)
        self.botao42.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao43 = QPushButton(self)
        self.botao43.move(100,200)
        self.botao43.resize(50,50)
        self.botao43.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao44 = QPushButton(self)
        self.botao44.move(150,200)
        self.botao44.resize(50,50)
        self.botao44.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao45 = QPushButton(self)
        self.botao45.move(200,200)
        self.botao45.resize(50,50)
        self.botao45.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao46 = QPushButton(self)
        self.botao46.move(250,200)
        self.botao46.resize(50,50)
        self.botao46.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao47 = QPushButton(self)
        self.botao47.move(300,200)
        self.botao47.resize(50,50)
        self.botao47.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao48 = QPushButton(self)
        self.botao48.move(350,200)
        self.botao48.resize(50,50)
        self.botao48.setStyleSheet('QPushButton{background-color:#ffffff}')
#linha05
        self.botao51 = QPushButton(self)
        self.botao51.move(0,150)
        self.botao51.resize(50,50)
        self.botao51.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao52 = QPushButton(self)
        self.botao52.move(50,150)
        self.botao52.resize(50,50)
        self.botao52.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao53 = QPushButton(self)
        self.botao53.move(100,150)
        self.botao53.resize(50,50)
        self.botao53.setStyleSheet('QPushButton{background-color:#ffffff}')
        
        self.botao54 = QPushButton(self)
        self.botao54.move(150,150)
        self.botao54.resize(50,50)
        self.botao54.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao55 = QPushButton(self)
        self.botao55.move(200,150)
        self.botao55.resize(50,50)
        self.botao55.setStyleSheet('QPushButton{background-color:#ffffff}')
        
        self.botao56 = QPushButton(self)
        self.botao56.move(250,150)
        self.botao56.resize(50,50)
        self.botao56.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao57 = QPushButton(self)
        self.botao57.move(300,150)
        self.botao57.resize(50,50)
        self.botao57.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao58 = QPushButton(self)
        self.botao58.move(350,150)
        self.botao58.resize(50,50)
        self.botao58.setStyleSheet('QPushButton{background-color:#000000}')
#linha06
        self.botao61 = QPushButton(self)
        self.botao61.move(0,100)
        self.botao61.resize(50,50)
        self.botao61.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao62 = QPushButton(self)
        self.botao62.move(50,100)
        self.botao62.resize(50,50)
        self.botao62.setStyleSheet('QPushButton{background-color:#ffffff}')
        
        self.botao63 = QPushButton(self)
        self.botao63.move(100,100)
        self.botao63.resize(50,50)
        self.botao63.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao64 = QPushButton(self)
        self.botao64.move(150,100)
        self.botao64.resize(50,50)
        self.botao64.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao65 = QPushButton(self)
        self.botao65.move(200,100)
        self.botao65.resize(50,50)
        self.botao65.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao66 = QPushButton(self)
        self.botao66.move(250,100)
        self.botao66.resize(50,50)
        self.botao66.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao67 = QPushButton(self)
        self.botao67.move(300,100)
        self.botao67.resize(50,50)
        self.botao67.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao68 = QPushButton(self)
        self.botao68.move(350,100)
        self.botao68.resize(50,50)
        self.botao68.setStyleSheet('QPushButton{background-color:#ffffff}')
#linha07
        self.botao71 = QPushButton(self)
        self.botao71.move(0,50)
        self.botao71.resize(50,50)
        self.botao71.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao72 = QPushButton(self)
        self.botao72.move(50,50)
        self.botao72.resize(50,50)
        self.botao72.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao73 = QPushButton(self)
        self.botao73.move(100,50)
        self.botao73.resize(50,50)
        self.botao73.setStyleSheet('QPushButton{background-color:#ffffff}')
        
        self.botao74 = QPushButton(self)
        self.botao74.move(150,50)
        self.botao74.resize(50,50)
        self.botao74.setStyleSheet('QPushButton{background-color:#000000}')

        self.botao75 = QPushButton(self)
        self.botao75.move(200,50)
        self.botao75.resize(50,50)
        self.botao75.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao76 = QPushButton(self)
        self.botao76.move(250,50)
        self.botao76.resize(50,50)
        self.botao76.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao77 = QPushButton(self)
        self.botao77.move(300,50)
        self.botao77.resize(50,50)
        self.botao77.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao78 = QPushButton(self)
        self.botao78.move(350,50)
        self.botao78.resize(50,50)
        self.botao78.setStyleSheet('QPushButton{background-color:#000000}')
#linha08
        self.botao81 = QPushButton(self)
        self.botao81.move(0,0)
        self.botao81.resize(50,50)
        self.botao81.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao82 = QPushButton(self)
        self.botao82.move(50,0)
        self.botao82.resize(50,50)
        self.botao82.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao83 = QPushButton(self)
        self.botao83.move(100,0)
        self.botao83.resize(50,50)
        self.botao83.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao84 = QPushButton(self)
        self.botao84.move(150,0)
        self.botao84.resize(50,50)
        self.botao84.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao85 = QPushButton(self)
        self.botao85.move(200,0)
        self.botao85.resize(50,50)
        self.botao85.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao86 = QPushButton(self)
        self.botao86.move(250,0)
        self.botao86.resize(50,50)
        self.botao86.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.botao87 = QPushButton(self)
        self.botao87.move(300,0)
        self.botao87.resize(50,50)
        self.botao87.setStyleSheet('QPushButton{background-color:#000000}')
        
        self.botao88 = QPushButton(self)
        self.botao88.move(350,0)
        self.botao88.resize(50,50)
        self.botao88.setStyleSheet('QPushButton{background-color:#ffffff}')

        self.CarregarJanela()
        
    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()
        
    def bt11(self):
        self.botao82.setStyleSheet('QPushButton{background-color:#000000}')





aplicacao = QApplication(sys.argv)
j = Janela()
##############################################################################################################################
#configuração servidor
@Pyro4.expose
class Botao:
    def bt01 (self):
        print ("--------------------> Dentro do Botao 01")
        #j.botao01.move(150,00)
        return (retornobt01())
    def bt02 (self):
        print ("--------------------> Dentro do Botao 02")
        return (retornobt02())

daemon = Pyro4.Daemon()
uri = daemon.register(Janela)
ns = Pyro4.locateNS()
ns.register('Botao', uri)
print (uri)
comunicar = threading.Thread(target=daemon.requestLoop)




'''
while (True):
    print ("oi")
    time.sleep(1)
'''

muda = threading.Thread(target=mudar)
#muda.start()






