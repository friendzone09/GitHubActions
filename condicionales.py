
import os

name = os.getenv('NOMBRE')
edad = int(os.getenv('EDAD'))

if edad >= 18:
    print(f'Hola {name} eres mayor de edad')
else:
    print(F'Hola {name} eres menor de edad')