import re

class Cliente:
    def __init__(self, numero_id, nombre, correo):
        # Asignación de valores a través de los setters para activar la validación
        self.numero_id = numero_id
        self.nombre = nombre
        self.correo = correo

    # --- Encapsulamiento y Validación para 'numero_id' ---
    @property
    def numero_id(self):
        return self.__numero_id

    @numero_id.setter
    def numero_id(self, valor):
        if not str(valor).isdigit():
            raise ValueError("El número de identificación debe contener solo dígitos.")
        self.__numero_id = str(valor)

    # --- Encapsulamiento y Validación para 'nombre' ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not str(valor).strip():
            raise ValueError("El nombre del cliente no puede estar vacío.")
        self.__nombre = str(valor).strip()

    # --- Encapsulamiento y Validación para 'correo' ---
    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        # Patrón simple para validar el formato del correo electrónico
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(patron, str(valor)):
            raise ValueError("Formato de correo electrónico no válido.")
        self.__correo = str(valor)

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.numero_id} | Correo: {self.correo})"

# --- Ejemplo de uso ---
try:
    cliente1 = Cliente("12345678", "Juan Perez", "juan.perez@ejemplo.com")
    print(cliente1)
except ValueError as e:
    print(f"Error: {e}")