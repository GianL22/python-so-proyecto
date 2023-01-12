import os
import time
from signal import signal, alarm, SIGALRM, pause

def handler(signum,frame):
    print('Mensaje enviado')

if __name__ == '__main__':
    #Se define el manejador cuando se recibe la señal de alarma
    signal(SIGALRM, handler);
    #Se crea el pipe
    r,w = os.pipe();
    #Se crea el proceso hijo c2, retorna 0 en el proceso hijo
    #y el id del proceso en el padre
    c2 = os.fork()
    
    if (c2 == 0):
    	#proceso hijo c2
    	#En c2 se cierra el extremo de escritura del pipe
    	os.close(w)
    	for i in range(10):
    	    #Se lee el mensaje del proceso c1
    	    text = os.read(r,50)
    	    print(text.decode())
    	    #print('Soy pid, c',i,'he recibido mensaje',text.decode())
    else:
        #Se crea el proceso hijo c1, retorna 0 en el proceso hijo
    	c1 = os.fork()
    	if (c1 == 0):
    	    #proceso hijo c1
    	    #En c1 se cierra el extremo de escritura del pipe
    	    os.close(r)
    	    for i in range(10):
    	    	#La alarma es enviada en cada 2 segundos
    	    	alarm(2);
    	    	#El proceso se retiene hasta que se reciba una señal
    	    	pause();
    	    	#C1 envia al extremo  del  
    	    	text = b"Mensaje recibido" 
    	    	os.write(w, text)
    	    	#print("Soy pid2, c",i,"he mandado mensaje y debe haber sido leido")
    	else:
    	    #El proceso se retiene hasta que todos sus procesos hijos terminen
            os.wait();
