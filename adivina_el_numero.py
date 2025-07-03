from random import randint

def pedir_nombre():
    while True:
        try:
            nombre = input("Ingresa tu nombre: ")
            return nombre
        except:
            print("Dato invalido")

def pedir_numero(peticion):
    while True:
        try:
            numero = int(input(peticion))
            return numero
        except:
            print("▲ Dato invalido")

def numero_aleatorio():
    while True:
        minimo = pedir_numero("Ingresa rango minimo: ")
        maximo = pedir_numero("Ingresa rango maximo: ")

        if minimo > maximo:
            print("El minimo no puede ser mayor que el maximo :S")
        else:
            break

    return randint(minimo, maximo)

def chequear_eleccion(eleccion, numero_secreto):
    if eleccion < numero_secreto:
        print(f"El numero oculto es mas grande")
        return False
        
    if eleccion > numero_secreto:
        print(f"El numero oculto es mas chico")
        return False

    if eleccion == numero_secreto:
        return True

def jugada(nombre, numero_secreto):
    intentos = 0 
    while intentos < 10: # 10 intentos por defecto, aunque se podria crear una funcion para elegir la cantidad de intentos
        eleccion = pedir_numero("Adivina el numero: ")
        intentos+=1
        resultado = chequear_eleccion(eleccion, numero_secreto)
        if resultado == True:
            print(f"Felicidades! Ganaste {nombre}! Solo te costo {intentos} intentos :)")
            break
    else:
        print("Perdiste :(")

def repetir_partida():
    while True:
        try:
            respuesta = input("Deseas comenzar una nueva partida? \n[1].Si\n[2].No\nRespuesta: ")
            if respuesta == '1':
                return True
            elif respuesta == '2':
                return False
            else:
                print("Ingresa un dato valido: (1) o (2)")
        except:
            print("▲ Dato invalido")
        
def main():
    while True:
        nombre = pedir_nombre()
        numero_secreto =  numero_aleatorio()
        jugada(nombre, numero_secreto)
        repetir = repetir_partida()
        if repetir == True:
            print("Buena eleccion!")
        else:
            print("Fin del programa")
            break

main()

