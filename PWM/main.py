# Programa de control mediante PWM de un LED, desde un ESP32DEVKIT

from machine import Pin, PWM
from time import sleep

frequency = 50
led = PWM(Pin(5),frequency)

while True:
    for dutyCycle in range(0,1024):
        led.duty(dutyCycle)
        sleep(0.005)