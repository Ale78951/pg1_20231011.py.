from gpiozero import LED 
from time import sleep
import psutil

Diccionario= {'rojo':LED(14),'verde':LED(15),'Amarillo':LED(16)}
while True:

    Porcentaje= input( psutil.cpu_percent(4))
    Diccionario['verde'].off()  
    Diccionario['rojo'].off()  
    Diccionario['Amarillo'].off()   

    if Porcentaje<=10:
        Diccionario['verde'].on()

    elif Porcentaje>10 and Porcentaje<20:
        Diccionario['Amarillo'].on()
    else :
        Diccionario['rojo'].on()
        sleep(1)
        Diccionario['rojo'].off()
        sleep(1)
        
