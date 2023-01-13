import sys
if __name__ == '__main__':
    #El numero de argumentos debe ser 3
    #El campo argv guarda, además de los argumentos, el nombre del presente script
    if len(sys.argv) == 4:
    	#Se guarda el bufsize y se valida su valor
        bufsize = int(sys.argv[1])
        if (0 < bufsize < 16385):
            #Se guardan las ubicaciones de los archivos de entrada y salida
            psource = sys.argv[2]
            ptarget = sys.argv[3]
            #Se abre el archivo de salida en modo de escritura con el bufersize
            ftarget = open(ptarget, "w", buffering = bufsize);
            #Se abre el archivo de entrada en modo de lectura con el bufersize
            with open(psource, buffering = bufsize) as fsource:
                while True: 
                    #Se lee el máximo de caracteres posibles con el bufsize definido
                    chunk = fsource.read(bufsize);
                    #Se detiene el ciclo cuando se leyó todo el contenido del archivo de entrada
                    if (chunk == ''):
                        break;
                    #Se escribe lo leido en el archivo de salida
                    ftarget.write(chunk);
            #Se cierran ambos archivos
            ftarget.close();    
            fsource.close();
        else:
            print("ERROR el valor bufsize debe estar dentro del rango 1 a 16384 ")
    else:
    	print("ERROR en el numero de argumentos")
