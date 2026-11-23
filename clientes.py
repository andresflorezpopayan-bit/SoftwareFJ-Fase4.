


class Cliente:

    def __init__(self, nombre, correo):

        self.nombre = nombre
        self.correo = correo

        self.validar()

    def validar(self):

        if not self.nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        if "@" not in self.correo:
            raise ClienteError(
                "Correo electrónico inválido"
            )

    def __str__(self):
        return f"{self.nombre} - {self.correo}"
    
