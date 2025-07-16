import os
import time


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def indice_masa_corporal(altura, peso, sistema="metrico"):
    limpiar_pantalla()
    mostrar_titulo()

    if sistema == "metrico":
        sistema_texto = "Sistema métrico"
        IMC = round((peso / altura**2), 2)
    else:
        sistema_texto = "Sistema imperial"
        IMC = round((peso / altura**2) * 703, 2)

    resultados = [
        f"Sistema empleado: {sistema_texto}",
        f"Altura: {altura}",
        f"Peso: {peso}",
        f"IMC: {IMC}"
    ]

    if IMC < 18.5:
        resultados.append("Estado: Bajo peso")
    elif IMC <= 24.9:
        resultados.append("Estado: Peso normal")
    elif IMC <= 29.9:
        resultados.append("Estado: Sobrepeso")
    else:
        resultados.append("Estado: Obesidad")

    ancho_max = max(len(linea) for linea in resultados)
    borde = "+" + "-" * (ancho_max + 2) + "+"

    def mostrar_resultado():
        print("\n" + borde)
        for linea in resultados:
            print(f"| {linea.ljust(ancho_max)} |")
        print(borde)

    mostrar_resultado()

    while True:
        print("\nEscribe [1] para regresar al menú principal.")
        opcion = input(">> ")
        if opcion == "1":
            print("🡐 Regresando al menú principal...")
            time.sleep(0.5)
            limpiar_pantalla()
            break
        else:
            limpiar_pantalla()
            mostrar_titulo()
            mostrar_resultado()
            print("\n❌ Opción inválida. Intenta de nuevo.")


def mostrar_titulo():
    print('''
  ___ __  __  ___ 
 |_ _|  \\/  |/ __|
  | || |\\/| | (__ 
 |___|_|  |_|\\___|
''')

def ingresar_numero(texto):
    while True:
        try:
            numero = float(input(texto))
            if numero <= 0:
                print("El valor ingresado debe ser mayor que 0")
            else:
                return numero
        except ValueError:
            print("Su respuesta debe ser un numero")
        except:
            print("Ingrese un dato valido")



def mostrar_opciones(diccionario):
    # Obtener el contenido formateado
    contenido = [f"[{clave}] - {valor}" for clave, valor in diccionario.items()]
    ancho_maximo = max(len(linea) for linea in contenido)
    borde_superior = "+" + "-" * (ancho_maximo + 2) + "+"
    print(borde_superior)
    for linea in contenido:
        print(f"| {linea.ljust(ancho_maximo)} |")

    print(borde_superior)

def eleccion(diccionario, texto):
    while True:
        opcion = input(texto)
        if opcion in diccionario.keys():
            match opcion:
                case '1':
                    limpiar_pantalla()
                    mostrar_titulo()
                    indice_masa_corporal(ingresar_numero("Ingrese altura (metros): "), ingresar_numero("Ingrese peso (Kilogramos): "))
                    break
                case '2':
                    limpiar_pantalla()
                    mostrar_titulo()
                    indice_masa_corporal(ingresar_numero("Ingrese altura (Pulgadas): "), ingresar_numero("Ingrese peso (Libras): "), sistema="imperial")
                    break
                case _:
                    limpiar_pantalla()
                    print("Fin del programa")
                    exit()
        else:
            print("Elija una opcion valida")
            time.sleep(0.8)
            limpiar_pantalla()
            mostrar_titulo()
            mostrar_opciones(diccionario)
            


def main():
    while True: 
        opciones = {'1': 'Sistema metrico', '2': 'Sistema imperial', '3':'Finalizar'}
        mostrar_titulo()
        mostrar_opciones(opciones)
        eleccion(opciones, "Ingresar: ")

main()
