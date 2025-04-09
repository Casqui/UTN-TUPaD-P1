import ast
import math
import os

"""
Práctivo 01 - Estructuras secuenciales

CASCO, Osvaldo Adrián
"""
# Establece una pausa
def esperar():
    input("\nPresione Enter para continuar...")

# Ingreso y validación de una edad
def ingresar_edad():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            if edad < 0:
                raise ValueError("La edad no puede ser un número negativo.\n")
            
            return edad
        except ValueError:
            print("La edad debe ser un número entero.\n")

# Ingreso y validación de número
def ingresar_numero(input_text, tipo, positivo = True, incluir_cero = False):
    while True:
        try:
            texto = input(input_text)
            if tipo is int and "." in texto:
                    raise ValueError("El valor debe ser un número entero.\n")

            ingreso = ast.literal_eval(texto)
            numero = tipo(ingreso)
            if not incluir_cero:
                if positivo and numero <= 0:
                    raise ValueError("El valor debe ser mayor a 0.\n")
                elif numero == 0:
                    raise ValueError("El valor no puede ser 0.\n")
            else:
                if positivo and numero < 0:
                    raise ValueError("El valor debe ser mayor o igual 0.\n")
            
            return numero
        except ValueError:
            if tipo is int:
                print("El valor debe ser un número entero.\n")
            elif tipo is float:
                print("El valor debe ser un número decimal.\n")
            else:
                print("El valor no es del tipo indicado.\n")

# Actividad 01
def actividad_01():
    print("Hola Mundo!")

# Actividad 02
def actividad_02():
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}!")

# Actividad 03
def actividad_03():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = ingresar_edad()
    residencia = input("Ingrese su lugar de residencia: ")
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Actividad 04
def actividad_04():
    radio = ingresar_numero("Ingrese el radio: ", float)
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio
    print(f"El área del círculo es: {area:.2f}")
    print(f"El perímetro del círculo es: {perimetro:.2f}")

# Actividad 05
def actividad_05():
    segundos = ingresar_numero("Ingrese la cantidad de segundos: ", int, incluir_cero=True)
    horas = segundos / 3600
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# Actividad 06
def actividad_06():
    multiplicando = ingresar_numero("Ingrese la tabla que desea: ", int)
    multiplicadores = ingresar_numero(f"Ingresar hasta que número desea la tabla del {multiplicando}: ", int)
    print(f"La tabla de multiplicar del {multiplicando} solicitada es:")
    for multiplicador in range(multiplicadores):
        print(f"{multiplicador + 1} x {multiplicando} = {(multiplicador + 1) * multiplicando}")

# Actividad 07
def actividad_07():
    a = ingresar_numero("Ingrese el primer número: ", int, False)
    b = ingresar_numero("Ingrese el segundo número: ", int, False)
    print(f"a + b = {a + b}")
    print(f"a / b = {(a / b):.2f}")
    print(f"a x b = {a * b}")
    print(f"a - b = {a - b}")

# Actividad 08
def actividad_08():
    altura = ingresar_numero("Ingrese su altura (en m): ", float)
    peso = ingresar_numero("Ingrese su peso (en kg): ", float)
    imc = peso / (altura ** 2)
    print(f"Su IMC es = {imc:.2f}")

# Actividad 09
def actividad_09():
    celcius = ingresar_numero("Ingrese la temperatura en °C: ", float, False, True)
    fahrenheit = (9/5) * celcius + 32
    print(f"La temperatura en °F es: {fahrenheit:.2f}°")

# Actividad 10
def actividad_10():
    primero = ingresar_numero("Ingrese el primer número: ", float, incluir_cero=True)
    segundo = ingresar_numero("Ingrese el segundo número: ", float, incluir_cero=True)
    tercero = ingresar_numero("Ingrese el tercer número: ", float, incluir_cero=True)
    promedio = (primero + segundo + tercero) / 3
    print(f"El promedio es: {promedio:.2f}")

    
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpiar_pantalla()
    print("""
    ===== ACTIVIDADES =====
    1. Actividad 1
    2. Actividad 2
    3. Actividad 3
    4. Actividad 4
    5. Actividad 5
    6. Actividad 6
    7. Actividad 7
    8. Actividad 8
    9. Actividad 9
    10. Actividad 10
    =======================
    0. Salir
    """)

def main():
    while True:
        menu()
        opcion = ingresar_numero("Ingrese una actividad: ", int, False, True)
        match opcion:
            case 0:
                break
            case 1:
                actividad_01()
            case 2:
                actividad_02()
            case 3:
                actividad_03()
            case 4:
                actividad_04()
            case 5:
                actividad_05()
            case 6:
                actividad_06()
            case 7:
                actividad_07()
            case 8:
                actividad_08()
            case 9:
                actividad_09()
            case 10:
                actividad_10()
            case _:
                print("Ha ingresado una opción inválida.")
        esperar()

if __name__ == "__main__":
    main()
