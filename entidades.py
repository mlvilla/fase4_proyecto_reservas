from abc import ABC, abstractmethod

class EntidadBase(ABC):

    def __init__(self, identificador):
        self._id = identificador

    @abstractmethod
    def mostrar_detalle(self):
        pass