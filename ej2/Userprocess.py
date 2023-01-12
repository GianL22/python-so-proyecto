#se importa el modulo os que provee funciones para interactuar con el sistema operativo
import os


if __name__ == '__main__':
    
    print('El numero de procesos del usuario es:')
    
    #Se ejecutan los comandos correspondientes en la terminal usando el metodo system
    #Es mostrado el nombre del usuario
    os.system('logname')
    #Es mostrado el numero maximo de procesos activos a la vez  
    os.system('ulimit -a | grep process')
