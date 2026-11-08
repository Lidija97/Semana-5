
from datetime import datetime


class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0
        self.saldo = 0
        self.nacionalidad = "Peruana"
        self.fecha_registro = datetime.now()

    def registrar(self):
        self.nombre = input("Ingrese su nombre: ")

        while True:
            try:
                edad = int(input("Ingrese su edad: "))

                if edad < 0:
                    print("Error: La edad no puede ser negativa.")
                else:
                    self.edad = edad
                    break

            except ValueError:
                print("Error: Ingrese un número entero válido.")

    def cumpleanos(self):
        self.edad += 1

    def mostrar_registro(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Saldo:", self.saldo)
        print("Nacionalidad:", self.nacionalidad)
        print("Fecha de registro:",
              self.fecha_registro.strftime("%d/%m/%Y %H:%M"))


persona1 = Persona()
persona1.registrar()

persona2 = Persona()
persona2.registrar()

persona1.cumpleanos()
persona2.cumpleanos()

print("\n--- Persona 1 ---")
persona1.mostrar_registro()

print("\n--- Persona 2 ---")
persona2.mostrar_registro()
