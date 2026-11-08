
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

    def consultar_saldo(self):
        print("Saldo de", self.nombre, ":", self.saldo)

    def transferir(self, destinatario, monto):
        try:
            monto = float(monto)

            if monto <= 0:
                print("Error: El monto debe ser mayor a cero.")
                return

            if monto > self.saldo:
                print("Error: Saldo insuficiente.")
                return

            self.saldo -= monto
            destinatario.saldo += monto

            print("Transferencia realizada correctamente.")

        except (ValueError, TypeError):
            print("Error: Ingrese un monto numérico válido.")


persona1 = Persona()
persona1.registrar()

persona2 = Persona()
persona2.registrar()

persona1.saldo = 500
persona2.saldo = 100

print("\n--- Saldos iniciales ---")
persona1.consultar_saldo()
persona2.consultar_saldo()

print("\n--- Transferencia válida ---")
persona1.transferir(persona2, 200)

print("\n--- Saldos actualizados ---")
persona1.consultar_saldo()
persona2.consultar_saldo()

print("\n--- Transferencia rechazada ---")
persona1.transferir(persona2, 1000)

print("\n--- Saldos finales ---")
persona1.consultar_saldo()
persona2.consultar_saldo()
