from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) #Rango de 0 a 3.3V

while True:
    potValue = pot.read()
    print(potValue)
    sleep(0.1)