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

