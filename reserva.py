from excepciones import ErrorEnReserva
import datetime

def guardar_log(texto):
    with open("bitacora.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now()}] {texto}\n")

class Reserva:
    def __init__(self, cliente, servicio, tiempo):
        self._cliente = cliente
        self._servicio = servicio
        self._tiempo = tiempo
        self._estado = "Creada"

    def procesar(self):
        try:
            if not self._cliente or not self._servicio:
                raise ErrorEnReserva("Datos incompletos.")

            pago = self._servicio.calcular_total(self._tiempo)

        except Exception as e:
            self._estado = "Fallida"
            guardar_log(f"Reserva fallida: {e}")
            raise ErrorEnReserva("No se pudo procesar la reserva") from e

        else:
            self._estado = "Confirmada"
            return f"Reserva de {self._cliente.nombres} lista. Pago: ${pago}"

        finally:
            guardar_log("Operación de reserva finalizada")
