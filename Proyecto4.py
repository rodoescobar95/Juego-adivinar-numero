from random import *
numero_secreto = randint(1,100)
print(numero_secreto)
nombre = (input("Escribe tu nombre "))
numero = int(input(f"Hola {nombre}, \nhe pensado un numero entre el 1 y 100, \ntienes 8 intentos para adivinarlo, inserta el numero "))
intentos = 1

while intentos < 8:
    if (numero < 1) or (numero > 100):
        print("Numero no permitido")
        intentos += 1
        numero = int(input("Inserta otro numero "))
        print(f"llevas {intentos} intentos")

    elif numero < numero_secreto:
        print("El numero que elegiste es menor que el numero secreto")
        intentos += 1
        numero = int(input("Inserta otro numero "))
        print(f"llevas {intentos} intentos")

    elif numero > numero_secreto:
        print("El numero que elegiste es mayor al numero secreto")
        intentos += 1
        numero = int(input("Inserta otro numero "))
        print(f"llevas {intentos} intentos")

    else:
        print(f"Has ganado {nombre}, te ha tomado {intentos} intentos")
        break
else:
    print(f"{nombre}, ya no te quedan intentos, el numero secreto era {numero_secreto}")