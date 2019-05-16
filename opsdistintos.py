import threading
#import time

class MyThread(threading.Thread):
    def __init__(self, x, y, numhilo):
        super(MyThread, self).__init__()
        self.a = x
        self.b = y
        self.hilo = numhilo

    def run(self): 
        print "Proceso hilo " + str(self.hilo) + ": " + str(self.operacion(self.a, self.b, self.hilo)) + "\n" 

    def operacion (self, x, y, hilo):
        if hilo==1:
            return x+y
        if hilo==2:
            return x-y
        if hilo==3:
            return x*y
        if hilo==4:
            return x/y

if __name__ == "__main__":
    threads = []
    n=input('Ingrese el primer numero: ')
    m=input('Ingrese el segundo numero: ')
    for i in range(4):
        t = MyThread(n,m,i+1)
        t.start()
        threads.append(t)
		
    for t in threads:
        t.join()
