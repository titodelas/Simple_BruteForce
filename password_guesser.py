# Importar los módulos necesarios
import itertools
import time

# Definir la función adivinar_contrasena()
def adivinar_contrasena(contrasena):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    longitud_maxima = 4
    encontrado = False
    intentos_fallidos = 0
    tiempo_inicio = time.time()
    for longitud in range(1, longitud_maxima + 1):
        combinaciones = itertools.product(caracteres, repeat=longitud)
        for combinacion in combinaciones:
            intento = "".join(combinacion)
            if intento == contrasena:
                print(f"La contraseña es {intento}")
                encontrado = True
                break
            else:
                intentos_fallidos += 1
        if encontrado:
            break

    tiempo_transcurrido = time.time() - tiempo_inicio
    print(f"Tiempo total: {tiempo_transcurrido:.2f} segundos")
    print(f"Número de intentos fallidos: {intentos_fallidos}")

# Pedir al usuario que introduzca una contraseña
contrasena = input("Introduce una contraseña: ")

# Llamar a la función adivinar_contrasena() con la contraseña proporcionada
adivinar_contrasena(contrasena)
