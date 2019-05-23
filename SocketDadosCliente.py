import socket  
  
s = socket.socket()   
s.connect(("192.168.8.208", 8001))  
s.send("Conectado a XXX-Chats.")

while (True):
    mensaje = raw_input("Desea lanzar los dados? y/n")

    if mensaje == 'y':
        mensaje = "Lanzar"
        s.send(mensaje)
        resultado = s.recv(1024)  
        print resultado
    if mensaje == 'n':
        mensaje = "Salir"
        s.send(mensaje)  
        break


s.close()  
