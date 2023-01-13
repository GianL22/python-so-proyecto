import os
#Es importado del modulo sys para captar los argumentos
import sys
from time import perf_counter
if __name__ == '__main__':
    #argv es el arreglo que posee el programa y sus parametros
    #Se evalua si se pasó el nombre programa a ejecutar
    if (len(sys.argv) > 1): 
    	#El primer elemento es el nombre del presente script, por lo tanto se elimina
        sys.argv.pop(0)
        #El programa y sus parametros son juntados en un string separados por un espacio
        programa = " ".join(sys.argv)
        print(programa)
        #Se inicia el contador
        start = perf_counter()
        #Se ejecuta el programa junto con sus argumentos
        os.system(programa)
        #Se detiene el contador
        end = perf_counter()
        print(end - start, 'segundos')
    else:
    	print('ERROR en los parametros pasados')
