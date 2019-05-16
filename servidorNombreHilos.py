from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import threading

class MyThread(threading.Thread):
    def __init__(self, nombre):
        super(MyThread, self).__init__()
        self.nombre = nombre
        self.mensaje=""

    def run(self):
        if self.nombre=="":
            self.mensaje= "Cual es tu nombre?"
        else:
            self.mensaje=  "Hola "+self.nombre+" te has conectado el "+ str(datetime.now())

class	Hilo:
    def Hilo(self, n):
            t = MyThread(n)
            t.start()
            return t.mensaje

server = SimpleXMLRPCServer(("192.168.9.80", 8001),allow_none=True)
server.register_instance(Hilo(), "Hilo")
server.serve_forever()