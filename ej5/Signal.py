import os
from signal import signal, alarm, SIGALRM, pause

def handler(signum,frame):
    print('Mensaje enviado')

if __name__ == '__main__':
    #Se define el manejador cuando se recibe la señal de alarma
    signal(SIGALRM, handler);
    #Se crea el pipe
    r,w = os.pipe();
    #Se crea el proceso hijo c2
    #Retorna 0 en el proceso hijo
    #Retorna el id del proceso hijo en el proceso del padre 
    c2 = os.fork()
    
    if (c2 == 0):
    	#proceso hijo c2
    	#En c2 se cierra el extremo de escritura del pipe
    	os.close(w)
    	for i in range(10):
    	    #Se lee e imprime el mensaje del proceso c1
    	    text = os.read(r,50)
    	    print(text.decode())
    else:
    	#proceso padre
        #Se crea el proceso hijo c1, retorna 0 en el proceso hijo
    	c1 = os.fork()
    	if (c1 == 0):
    	    #proceso hijo c1
    	    #En c1 se cierra el extremo de escritura del pipe
    	    os.close(r)
    	    for i in range(10):
    	    	#La alarma es enviada en cada 2 segundos
    	    	alarm(2);
    	    	#El proceso se retiene hasta que se reciba una señal SIGALRM
    	    	pause();
    	    	text = b"Mensaje recibido" 
    	    	#C1 envia un mensaje al proceso C2  
    	    	os.write(w, text)
    	else:
    	    #proceso padre
    	    #El proceso se retiene hasta que todos sus procesos hijos terminen
            os.wait();
