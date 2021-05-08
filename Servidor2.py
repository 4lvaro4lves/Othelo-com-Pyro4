import Pyro4
import time
#
print ("\n\n-------------->>  CLIENTE  <<--------------\n\n")
Tempo=time.time()

ns = Pyro4.locateNS()
uri = ns.lookup('Janela')
o = Pyro4.Proxy(uri)

print ("Final de Tudo.")
print(time.time()-Tempo)

#o.bt01()
