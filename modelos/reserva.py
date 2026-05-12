# --- Excepciones Personalizadas ---
class ErrorReserva(Exception):
    """Clase base para excepciones relacionadas con reservas."""
    pass

class ErrorEstadoReserva(ErrorReserva):
    """Se lanza cuando una transición de estado no es válida."""
    pass


# --- Clase Reserva ---
class Reserva:
    def __init__(self, id_reserva, cliente, fecha, detalles):
        self.id_reserva = id_reserva
        self.cliente = cliente  # Se espera que sea un objeto de la clase Cliente
        self.fecha = fecha
        self.detalles = detalles
        self.estado = "Pendiente"  # Estados posibles: Pendiente, Confirmada, Cancelada

    def confirmar(self):
        """Confirma la reserva si su estado actual es Pendiente."""
        if self.estado == "Confirmada":
            raise ErrorEstadoReserva(f"La reserva {self.id_reserva} ya está confirmada.")
        elif self.estado == "Cancelada":
            raise ErrorEstadoReserva(f"No se puede confirmar la reserva {self.id_reserva} porque fue cancelada.")
        
        self.estado = "Confirmada"
        print(f"Éxito: Reserva {self.id_reserva} confirmada para {self.cliente.nombre}.")

    def cancelar(self):
        """Cancela la reserva si no ha sido cancelada previamente."""
        if self.estado == "Cancelada":
            raise ErrorEstadoReserva(f"La reserva {self.id_reserva} ya está cancelada.")
        
        self.estado = "Cancelada"
        print(f"Éxito: La reserva {self.id_reserva} ha sido cancelada.")

    def __str__(self):
        return f"Reserva #{self.id_reserva} | Estado: {self.estado} | Fecha: {self.fecha} | Cliente: {self.cliente.nombre}"