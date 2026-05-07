# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/cliente.py
# Responsable: Cristian
# Descripción: Clase Cliente con encapsulación y validaciones robustas.
# =============================================================================

import re
from modelos.entidad_base import EntidadBase
from excepciones.excepciones_personalizadas import ClienteInvalidoError
from utils.logger import log_info, log_warning, log_error


class Cliente(EntidadBase):
    """
    Clase que representa un cliente de Software FJ.
    Hereda de EntidadBase e implementa encapsulación total
    de datos personales con validaciones estrictas.
    """

    def __init__(self, nombre: str, correo: str, telefono: str):
        """
        Constructor del cliente.

        Args:
            nombre (str)  : Nombre completo del cliente.
            correo (str)  : Correo electrónico válido.
            telefono (str): Teléfono numérico de mínimo 7 dígitos.

        Raises:
            ClienteInvalidoError: Si algún dato no cumple las validaciones.
            ParametroFaltanteError: Si el nombre está vacío (desde EntidadBase).
        """
        super().__init__(nombre)
        self.__correo = correo
        self.__telefono = telefono

    # ─────────────────────────────────────────
    #  GETTERS Y SETTERS (Encapsulación)
    # ─────────────────────────────────────────

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        if not nuevo_correo or "@" not in nuevo_correo or "." not in nuevo_correo:
            raise ClienteInvalidoError(
                f"El correo '{nuevo_correo}' no tiene un formato válido."
            )
        self.__correo = nuevo_correo

    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str):
        if not nuevo_telefono or not nuevo_telefono.isdigit() or len(nuevo_telefono) < 7:
            raise ClienteInvalidoError(
                f"El teléfono '{nuevo_telefono}' debe ser numérico y tener mínimo 7 dígitos."
            )
        self.__telefono = nuevo_telefono

    # ─────────────────────────────────────────
    #  MÉTODOS ABSTRACTOS IMPLEMENTADOS
    # ─────────────────────────────────────────

    def validar(self) -> bool:
        """
        Valida todos los datos del cliente de forma estricta.

        Returns:
            bool: True si todos los datos son válidos.

        Raises:
            ClienteInvalidoError: Si algún dato es inválido.
        """
        try:
            # Validar nombre
            if not self.nombre or not self.nombre.strip():
                raise ClienteInvalidoError("El nombre del cliente no puede estar vacío.")

            # Validar correo con expresión regular
            patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
            if not re.match(patron_correo, self.__correo):
                raise ClienteInvalidoError(
                    f"El correo '{self.__correo}' no tiene un formato válido."
                )

            # Validar teléfono
            if not self.__telefono.isdigit() or len(self.__telefono) < 7:
                raise ClienteInvalidoError(
                    f"El teléfono '{self.__telefono}' debe ser numérico y tener mínimo 7 dígitos."
                )

        except ClienteInvalidoError:
            raise
        except Exception as e:
            raise ClienteInvalidoError(f"Error inesperado al validar cliente: {e}") from e
        else:
            log_info(f"Cliente '{self.nombre}' validado correctamente.")
            return True
        finally:
            log_info(f"Validación de cliente '{self.nombre}' finalizada.")

    def mostrar_info(self) -> str:
        """
        Retorna una cadena con la información completa del cliente.
        """
        estado = "Activo" if self.activo else "Inactivo"
        return (
            f"[Cliente ID: {self.id}] "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono} | "
            f"Estado: {estado} | "
            f"Registrado: {self.fecha_creacion}"
        )

    def __str__(self) -> str:
        return self.mostrar_info()
