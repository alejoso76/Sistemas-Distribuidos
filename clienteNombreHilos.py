import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://192.168.9.80:8001') 
#nombre = input('Ingrese su nombre: ')

print(s.Hilo(""))
nombre = input()
print(s.Hilo(nombre))
