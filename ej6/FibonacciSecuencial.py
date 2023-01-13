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

if __name__ == '__main__':
    #Se imprime el valor final
    print(fibonacci(nInicial(),1000000));
