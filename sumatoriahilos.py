import threading
#import time

class MyThread(threading.Thread):
    def __init__(self, inicio, fin):
        super(MyThread, self).__init__()
        self.inicio = inicio
        self.fin = fin
        self.total = 0

    def run(self): 
        self.sumatoria()

    def sumatoria (self):
        while(self.inicio <= self.fin):
            self.total += self.inicio
            self.inicio += 1
        return self.total

if __name__ == "__main__":
    threads = []
    totalS = 0
    for i in range(10):
        inicio = 10*i + 1
        fin = 10*i + 10
        t = MyThread(inicio, fin)
        t.start()
        threads.append(t)
		
    for t in threads:
        totalS += t.sumatoria()
        t.join()

    print "Sumatoria numeros 0-100 = "+str(totalS)

    

 
