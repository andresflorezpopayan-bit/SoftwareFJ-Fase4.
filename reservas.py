from excepciones import ReservaError
 
 
class Reserva:
 
def __init__(
self,
cliente,
servicio,
duracion
):
 
self.cliente = cliente
self.servicio = servicio
self.duracion = duracion
self.estado = "Pendiente"
 
def confirmar(self):
 
if self.duracion <= 0:
raise ReservaError(
"Duración inválida"
)
 
self.estado = "Confirmada"
 
def cancelar(self):
 
self.estado = "Cancelada"
 
def procesar(self):
 
try:
 
self.confirmar()
 
except Exception as error:
 
raise ReservaError(
"Error procesando la reserva"
) from error
 
finally:
 
print(
"Proceso de reserva finalizado"
)
