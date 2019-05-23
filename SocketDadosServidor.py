import socket
import random

Mi_socket=socket.socket()
Mi_socket.bind(("192.168.8.208", 8001))
Mi_socket.listen(1)  
print ("Servidor arriba, pero triste porque no tengo conexiones. pero sigo escuchando!!!!!")

sc, addr = Mi_socket.accept()
while (True):
	recibido = sc.recv(1024)  
	print ("Recibido: ", recibido)  
	if recibido=="Lanzar":
		x=random.randint(1,6)
		y=random.randint(1,6)
		sc.send(str(x)+":"+str(y))
		print ("Enviado: ", x," y ", y) 
	if recibido=="Salir":
		break 
sc.close()
Mi_socket.close()  
