import xmlrpc.client

a =int(input('Ingrese el primer numero: '))
b=int(input('Ingrese el segundo numero: '))
s = xmlrpc.client.ServerProxy('http://192.168.8.229:8001') 
print("la suma es: " + str(s.suma(a,b)))
