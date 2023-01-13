#Se importa el modulo threading que ofrece una abstracción para facilitar el manejo de hilos
import threading
import time
import random

#Genera un valor inicial entre 0 y 19
def nInicial(): 
    return random.randrange(0,20); 

#Calcula sucesión de fibonacci
def fibonacci(a,n):
    b = a + 1;
    for i in range(n):
        c = a + b;
        a = b;
        b = c;
    return c;

#Se crea una clase miHilo que posee el campo sun que guarda su propia sucesión fibonacci 
class miHilo (threading.Thread):
    #Se refina constructor de la clase thread, se agregan los campos:
    #    sum : Guarda el total de la sucesión 
    #    n   : número de terminos de la sucesion 
    #    inicio: número inicial de la sucesión
    def __init__(self, inicio, n):
        threading.Thread.__init__(self)
        self.sum = 0
        self.n = n
        self.inicio = inicio;
    #Se sobreescribe el metodo run de la clase Thread con la finalidad de guardar el resultado del fibonacci
    def run(self):
        self.sum = fibonacci(self.inicio, self.n)
        
if __name__ == '__main__':
    hilos = []
    resultado = 0
    inicial = nInicial();
    #Se instancian 20 objetos de las clase miHilo    
    for i in range(20):
        hilos.append(miHilo(inicial, 50000))
        #Se inician los hilos, el metodo start dispara el método run de la clase miHilo 
        hilos[i].start()
    #Se espera que todos los hilos terminen su ejecución
    for hilo in hilos:
        hilo.join()
    #Cuando todos los hilos han calculado las sucesiones, se totaliza el resultado accediendo al campo sum de cada hilo
    for hilo in hilos:
        resultado += hilo.sum;
    print(resultado)
