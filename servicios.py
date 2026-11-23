from abc import ABC, abstractmethod
from excepciones import ServicioError


class Servicio(ABC):

    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):

    def __init__(self, horas):

        super().__init__("Reserva de Sala")

        if horas <= 0:
            raise ServicioError(
                "Horas inválidas"
            )

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50000

    def descripcion(self):
        return "Reserva de sala empresarial"


class AlquilerEquipo(Servicio):

    def __init__(self, dias):

        super().__init__("Alquiler de Equipos")

        if dias <= 0:
            raise ServicioError(
                "Días inválidos"
            )

        self.dias = dias

    def calcular_costo(self):
        return self.dias * 80000

    def descripcion(self):
        return "Alquiler de equipos tecnológicos"


class AsesoriaEspecializada(Servicio):

    def __init__(self, horas):

        super().__init__("Asesoría")

        if horas <= 0:
            raise ServicioError(
                "Horas inválidas"
            )

        self.horas = horas

    def calcular_costo(self):
        return self.horas * 120000

    def descripcion(self):
        return "Asesoría especializada"
