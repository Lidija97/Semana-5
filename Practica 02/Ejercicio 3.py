
def solicitar_valores():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2

        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")


def dividir(a, b):
    return a / b


def sumar(a, b):
    return a + b


def registrar_elementos():
    while True:
        try:
            n = int(input("¿Cuántos elementos desea registrar?: "))

            if n <= 0:
                print("Error: Ingrese una cantidad mayor a cero.")
            else:
                break

        except ValueError:
            print("Error: Ingrese un número entero válido.")

    lista = []

    for i in range(n):
        elemento = input("Ingrese el elemento {}: ".format(i))
        lista.append(elemento)

    return lista


def consultar_elemento(lista, indice):
    if indice < 0:
        raise IndexError("El índice no puede ser negativo.")

    return lista[indice]


def main():
    print("--- OPERACIONES MATEMÁTICAS ---")

    while True:
        num1, num2 = solicitar_valores()

        try:
            resultado_suma = sumar(num1, num2)
            resultado_division = dividir(num1, num2)

        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

        except TypeError:
            print("Error: Tipos de datos incompatibles.")

        else:
            print("Resultado de la suma:", resultado_suma)
            print("Resultado de la división:", resultado_division)
            break

        finally:
            print("Proceso de operaciones finalizado.")

    print("\n--- REGISTRO DE ELEMENTOS ---")

    lista = registrar_elementos()
    print("Lista registrada:", lista)

    while True:
        try:
            indice = int(input("Ingrese el índice a consultar: "))
            elemento = consultar_elemento(lista, indice)

        except ValueError:
            print("Error: Ingrese un índice numérico entero.")

        except IndexError:
            print("Error: El índice no existe en la lista.")

        else:
            print("Elemento encontrado:", elemento)
            break

        finally:
            print("Consulta realizada.")

    print("\n--- PRUEBAS ADICIONALES ---")

    print("Prueba 1: Suma válida")
    print("Resultado:", sumar(10, 5))

    print("Prueba 2: División entre cero")
    try:
        print(dividir(10, 0))
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    print("Prueba 3: Tipos incompatibles")
    try:
        print(sumar("hola", 5))
    except TypeError:
        print("Error: Tipos de datos incompatibles.")


main()
