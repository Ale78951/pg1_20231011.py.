from gpiozero import LED 
from time import sleep

led=LED(14)

while true:
    led.on()
    sleep(1)
    led.off()
    sleep(1)


