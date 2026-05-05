from abc import ABC, abstractmethod

# Clase base general
class EntidadBase(ABC):
    def __init__(self, identificador):
        self._id = identificador  # protegido, no privado


# -------------------------
# metodos con abstraccion
# -------------------------

    @abstractmethod
    def mostrar_detalle(self):
        pass

# -------------------------
# Clase abstracta Servicio
# -------------------------

class Servicio(EntidadBase):
    def __init__(self, identificador, nombre, costo_base):
        super().__init__(identificador)
        self.__nombre = nombre          # privado
        self.__costo_base = costo_base  # privado


    # GETTERS para acceder a las clases hijas
    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_base(self):
        return self.__costo_base

    @abstractmethod
    def calcular_total(self, cantidad, extra=0):
        pass


# Primer servicio 
class ReservaSala(Servicio):
    def calcular_total(self, horas, descuento=0):
        return (self.costo_base * horas) - descuento

    def mostrar_detalle(self):
        return f"Sala de Espera: {self.nombre}"


# Segundo servicio 
class AlquilerEquipo(Servicio):
    def calcular_total(self, dias, impuesto=0.19):
        return (self.costo_base * dias) * (1 + impuesto)

    def mostrar_detalle(self):
        return f"Equipo: {self.nombre}"


# Tercer servicio 
class Asesoria(Servicio):
    def calcular_total(self, horas, virtual=False):
        ajuste = 0.8 if virtual else 1.0
        return (self.costo_base * horas) * ajuste

    def mostrar_detalle(self):
        return f"Asesoría: {self.nombre}"
