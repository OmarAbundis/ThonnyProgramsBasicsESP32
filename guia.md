# Guía de programación en Thonny Python

En está guía se muestran una serie de ejercicios básicos de programación utilizando Thonny Python, para controlar un **ESP32 DEVKIT.**

## PWM

En este sencillo ejercicio se controlará la intensidad lumínica de un LED, mediante modulación de ancho de pulso (PWM, por sus siglas en inglés). Está técnica emula la conversión de una señal digital en una señal analógica, mediante el control del ciclo de trabajo (*Duty Cycle*).

### Pasos a seguir

1. Hay que identificar en el [PINOUT](https://circuits4you.com/2018/12/31/esp32-devkit-esp32-wroom-gpio-pinout/), cual de sus terminales permite ser usada para modular pulsos.
2. Importar las clases Pin y PWM, del módulo **machine.**
`from machine import Pin, PWM`
3. Después, crear un objeto **PWM** llamado **led.**
`led = PWM(Pin(5),frequency)`

El valor de frecuencia puede ser desde 0 hasta 78125Hz.

4. Establecer el parámetro `duty_cycle`, que es la cantidad de tiempo.
`led.duty_cycle()`

La duty cycle debe estar entre 0 y 1023, que corresponden a 0 y 100%, respectivamente.

5. Dentro del *while* se crea un ciclo *for* para incrementar progresivamente el *duty cycle* desde 0 al 100% en intervalor de 100ms y trabajando a una frecuencia de 50Hz.

```
while True:
    for dutyCycle in range(0,1024):
    led.duyt(dutyCycle)
    sleep(0.005)
```
**Nota:**
La función *range()* tiene la siguiente sintaxis:

```
range(star, stop, step)
```
* **star** Es un número que especifica en qué posición comenzar. En nuestro caso desde 0.

* **stop** Es el número que indica en qué posición queremos que se detenga, como va a ser el 1023 y se va incrementando de uno en uno, el valor final es 1024.

* **step** Es un número entero que especifica el incremento y por defecto es 1.

## Lecturas analógicas

El ESP32DEVKIT tiene 15 líneas que se pueden emplear para introducir señales analógicas, así que hay que consultar el PINOUT, para identificar la entrada analógica.

El ESP32 DEVKIT tiene un ADC con una resolución de 12 bits y el rango de voltje de la señal analógica va de 0 a 3.3Vcd, así que hay que tener mucho cuidado de no exceder el límite para no dañar el dispositivo.

### Pasos a seguir

1. Para leer las entradas analógicas se importan las clases **ADC** y **Pin** del módulo **machine.**

`from machine import ADC, Pin`
`from time import sleep`


2. Se crea un objeto ADC para que adquiera el valor a través de la GPIO 34, y se le asigna a la variable de nombre **pot.**

`pot=ADC(Pin(34))`

3. Para leer el rango completo de voltaje, 0 a 3.3V, es necesario establecer la relación de atenuación de **11dB**, mediante el método **atten()**, los argumentos validos son los siguientes:

* **ADC.ATTN_0DB** - el voltaje de rango completo es de 1.2V.
* **ADC.ATTN_2_5DB** - el voltaje de rango completo es de 1.5V.
* **ADC.ATTN_6DB** - el voltaje de rango completo es de 2.0V.
* **ADC.ATTN_11DB** - el voltaje de rango completo es de 3.3V.

Si lo que se desea es cambiar la resolución mediante el número de bits de la conversión, se usa el método **width**, de la siguiente manera:

* **ADC.WIDTH_9BIT** - implica un rango de 0 a 511.
* **ADC.WIDTH_10BIT** - implica un rango de 0 a 1023.
* **ADC.WIDTH_11BIT** - implica un rango de 0 a 2047.
* **ADC.WIDTH_12BIT** - implica un rango de 0 a 4095.

Ejemplo:

`ADC.width(ADC.WIDTH_12BIT)`

4. El código completo queda asi:

```
from machine import Pin, ADC
from time import sleep

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB)

while True:
    potValue = pot.read()
    print(potValue)
    sleep(0.1)
```
