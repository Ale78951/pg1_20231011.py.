from gpiozero import LED 
from time import sleep

Diccionario= {'rojo':LED(14),'verde':LED(15),'azul':LED(16)}
color:str=input("Seleccione un color verde,rojo o azul")
parpadeo:str= input("Desea que el led parpadee si o no")

Diccionario[color].on()
sleep(4)
while True:

    
    if parpadeo=="si":
        Diccionario[color].on()
        sleep(1)
        Diccionario[color].off()
        sleep(1)
    
    


