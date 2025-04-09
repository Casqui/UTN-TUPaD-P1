from statistics import mode, median, mean
import ast
import random
import os

"""
Práctivo 03 - Estructuras condicionales

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
        except SyntaxError:
            print("La edad ingresada no posee un formato válido.\n")
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
        except SyntaxError:
            print("El valor ingresado no posee un formato válido.\n")
        except ValueError:
            if tipo is int:
                print("El valor debe ser un número entero.\n")
            elif tipo is float:
                print("El valor debe ser un número decimal.\n")
            else:
                print("El valor no es del tipo indicado.\n")

# Actividad 01
def actividad_01():
    edad = ingresar_edad()
    print(f"Es {"mayor" if edad > 18 else "menor"} de edad")

# Actividad 02
def actividad_02():
    nota = ingresar_numero("Ingrese su nota: ", int, incluir_cero=True)
    print("Aprobado" if nota >= 6 else "Desaprobado")

# Actividad 03
def actividad_03():
    numero = ingresar_numero("Ingrese un número: ", int, False, True)
    print("Ha ingresado un número par" if numero % 2 == 0 else "Por favor, ingrese un número par")

# Actividad 04
def actividad_04():
    edad = ingresar_edad()
    texto = ""
    if edad < 12:
        texto = "Niño/a"
    elif edad >= 12 and edad < 18:
        texto = "Adolescente"
    elif edad >= 18 and edad < 30:
        texto = "Adulto/a joven"
    else:
        texto = "Adulto/a"
    
    print(texto)

# Actividad 05
def actividad_05():
    contrasenia = input("Ingrese una contraseña: ")
    length = len(contrasenia)
    print("Ha ingresado una contraseña correcta" if 8 <= length <= 14 else "Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Actividad 06
def actividad_06():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    media = mean(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    modo = mode(numeros_aleatorios)
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Modo: {modo}")
    if media > mediana > modo:
        print("Sesgo positivo")
    elif media < mediana < modo:
        print("Sesgo negativo")
    else:
        print("Sin sesgo")


# Actividad 07
def actividad_07():
    palabra = input("Ingrese una frase o palabra: ")
    signo = "!" if len(palabra) > 0 and palabra[-1].lower() in 'aeiouáéíóúü' else ""
    print(f"{palabra}{signo}")

# Actividad 08
def actividad_08():
    nombre = input("Ingrese su nombre: ")
    while True:
        print("""
\n===== CONVERSIONES =====
1. MAYÚSCULAS
2. minúsculas
3. Título
=======================
        """)
        conversion = ingresar_numero("Ingrese una conversión: ", int, False, True)
        if conversion == 1:
            print(nombre.upper())
            break
        elif conversion == 2:
            print(nombre.lower())
            break
        elif conversion == 3:
            print(nombre.title())
            break
        else:
            print("\nHa ingresado una opción invalida.")

# Actividad 09
def actividad_09():
    magnitud = ingresar_numero("Ingrese la magnitud del terremoto: ", float)
    if magnitud < 3.0:
        print("Muy leve")
    elif 3.0 <= magnitud < 4.0:
        print("Leve")
    elif 4.0 <= magnitud < 5.0:
        print("Moderado")
    elif 5.0 <= magnitud < 6.0:
        print("Fuerte")
    elif 6.0 <= magnitud < 7.0:
        print("Muy fuerte")
    elif magnitud >= 7.0:
        print("Extremo")

# Actividad 10
def actividad_10():
    hemisferio = ""
    while True:
        hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").lower()
        if hemisferio in 'sn':
            break
        else:
            print("\nHa ingresado un hemisferio inválido.\n")
    
    while True:
        mes = input("Ingrese el mes del año: ").lower()
        if mes in {"enero", "ene", "01", "1"}:
            mes = "1"
        elif mes in {"febrero", "feb", "02", "2"}:
            mes = "2"
        elif mes in {"marzo", "mar", "03", "3"}:
            mes = "3"
        elif mes in {"abril", "abr", "04", "4"}:
            mes = "4"
        elif mes in {"mayo", "may", "05", "5"}:
            mes = "5"
        elif mes in {"junio", "jun", "06", "6"}:
            mes = "6"
        elif mes in {"julio", "jul", "07", "7"}:
            mes = "7"
        elif mes in {"agosto", "ago", "08", "8"}:
            mes = "8"
        elif mes in {"septiembre", "setiembre", "sep", "set", "09", "9"}:
            mes = "9"
        elif mes in {"octubre", "oct", "10"}:
            mes = "10"
        elif mes in {"noviembre", "nov", "11"}:
            mes = "11"
        elif mes in {"diciembre", "dic", "12"}:
            mes = "12"
        else:
            mes = "0"
        
        mes = int(mes)
        if mes <= 0 or mes > 12:
            print("\nHa ingresado un mes inválido.\n")
            continue
        
        dia = 0
        while True:
            dia = ingresar_numero("Ingrese el día del mes: ", int)
            if mes == 2 and dia > 29:
                print("\nEl día debe ser un valor entre 1 y 29.\n")
            elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
                print("\nEl día debe ser un valor entre 1 y 30.\n")
            elif dia > 31:
                print("\nEl día debe ser un valor entre 1 y 31.\n")
            else:
                break
        
        if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
            print("Invierno" if hemisferio == "n" else "Verano")
            break
        elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
            print("Primavera" if hemisferio == "n" else "Otoño")
            break
        elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
            print("Verano" if hemisferio == "n" else "Invierno")
            break
        else:
            print("Otoño" if hemisferio == "n" else "Primavera")
            break

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
