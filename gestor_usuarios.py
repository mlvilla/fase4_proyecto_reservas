from cliente import Cliente
from excepciones import ErrorDeDocumento
import datetime

# -------------------------
# Función para registrar logs
# # -------------------------
#  
def guardar_log(texto):
    with open("bitacora.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {texto}\n")

class GestorUsuarios:
    def __init__(self):
        self._lista = []
        self._precargar()


    # -------------------------
    # Precarga de datos iniciales
    # -------------------------

    def _precargar(self):
        try:
            self._lista.append(Cliente("John", "Alvarez", "1010", "3000000000", "Anserma"))
            self._lista.append(Cliente("Leonardo", "Alvarez", "2020", "3100000000", "Anserma"))
            self._lista.append(Cliente("Cesar", "Giraldo", "3030", "3200000000", "Anserma"))
            self._lista.append(Cliente("Jenny", "Aricapa", "4040", "3300000000", "Anserma"))
            guardar_log("Precarga de clientes exitosa")
        except Exception as e:
            guardar_log(f"Error precargando datos: {e}")



    # Buscar cliente por cédula
    
    def buscar(self, cedula):
        for c in self._lista:
            if c.documento_identidad == cedula:
                return c
        return None



    # Registrar cliente con manejo avanzado de excepciones

    def registrar(self, n, a, d, t, dir):
        try:
            # Validar duplicado
            if self.buscar(d):
                raise ErrorDeDocumento("El documento ya está registrado")

            # Intentar crear el cliente
            nuevo = Cliente(n, a, d, t, dir)

        except Exception as e:
            # Registrar el error real en la bitácora
            guardar_log(f"Error registrando cliente {d}: {e}")

            # Re-lanzar el error original para que el GUI lo muestre
            raise e

        else:
            # Si todo salió bien, agregar a la lista
            self._lista.append(nuevo)
            guardar_log(f"Cliente registrado correctamente: {d}")
            return nuevo

        finally:
            guardar_log("Operación de registro finalizada")
