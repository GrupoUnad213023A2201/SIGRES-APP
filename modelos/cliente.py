# =============================================================================
# SIGRES - Software FJ
# Archivo: modelos/cliente.py
# Responsable: Cristian
# Descripción: Clase Cliente con encapsulación total y validaciones robustas.
#              Hereda de EntidadBase para obtener ID autogenerado, fecha de
#              creación y estado activo/inactivo.
# =============================================================================

import re
from modelos.entidad_base import EntidadBase
from excepciones.excepciones_personalizadas import ClienteInvalidoError, ParametroFaltanteError
from utils.logger import log_info, log_warning, log_error


class Cliente(EntidadBase):
    """
    Clase que representa un cliente de Software FJ.

    Hereda de EntidadBase e implementa encapsulación total de datos
    personales con validaciones estrictas mediante expresiones regulares.

    Atributos privados:
        __correo   (str): Correo electrónico del cliente.
        __telefono (str): Número de teléfono del cliente.
    """

    def __init__(self, nombre: str, correo: str, telefono: str):
        """
        Constructor del cliente.

        Llama al constructor de EntidadBase para autogenerar el ID,
        la fecha de creación y el estado activo.

        Args:
            nombre   (str): Nombre completo del cliente.
            correo   (str): Correo electrónico válido.
            telefono (str): Teléfono numérico de mínimo 7 dígitos.

        Raises:
            ParametroFaltanteError: Si el nombre está vacío (desde EntidadBase).
            ClienteInvalidoError  : Si correo o teléfono son inválidos.
        """
        # Llama al constructor de EntidadBase que valida y asigna el nombre,
        # autogenera el ID único y registra la fecha de creación
        super().__init__(nombre)

        # Asigna los atributos privados del cliente
        self.__correo = correo
        self.__telefono = telefono

    # ─────────────────────────────────────────
    #  GETTERS Y SETTERS (Encapsulación)
    # ─────────────────────────────────────────

    @property
    def correo(self) -> str:
        """Retorna el correo electrónico del cliente."""
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        """
        Actualiza el correo con validación de formato.

        Raises:
            ClienteInvalidoError: Si el correo no tiene formato válido.
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        if not nuevo_correo or not re.match(patron, nuevo_correo):
            raise ClienteInvalidoError(
                f"El correo '{nuevo_correo}' no tiene un formato válido."
            )
        self.__correo = nuevo_correo

    @property
    def telefono(self) -> str:
        """Retorna el teléfono del cliente."""
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str):
        """
        Actualiza el teléfono con validación.

        Raises:
            ClienteInvalidoError: Si el teléfono no es numérico o es muy corto.
        """
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
        Implementa el método abstracto de EntidadBase.
        Valida todos los datos del cliente de forma estricta.

        Usa bloque try/except/else/finally para:
            - try     : Ejecutar todas las validaciones
            - except  : Capturar y relanzar errores de validación
            - else    : Registrar éxito si no hubo errores
            - finally : Registrar siempre que la validación finalizó

        Returns:
            bool: True si todos los datos son válidos.

        Raises:
            ClienteInvalidoError  : Si correo o teléfono son inválidos.
            ParametroFaltanteError: Si el nombre está vacío.
        """
        try:
            # Validar que el nombre no esté vacío
            if not self.nombre or not self.nombre.strip():
                raise ParametroFaltanteError("nombre")

            # Validar correo con expresión regular
            patron_correo = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
            if not re.match(patron_correo, self.__correo):
                raise ClienteInvalidoError(
                    f"El correo '{self.__correo}' no tiene un formato válido."
                )

            # Validar teléfono: solo dígitos y mínimo 7 caracteres
            if not self.__telefono.isdigit() or len(self.__telefono) < 7:
                raise ClienteInvalidoError(
                    f"El teléfono '{self.__telefono}' debe ser numérico y tener mínimo 7 dígitos."
                )

        except (ClienteInvalidoError, ParametroFaltanteError) as e:
            # Registra el error en el log y relanza la excepción
            log_error(f"Error al validar cliente '{self.nombre}': {e}")
            raise

        except Exception as e:
            # Captura cualquier error inesperado durante la validación
            log_error(f"Error inesperado al validar cliente '{self.nombre}': {e}")
            raise ClienteInvalidoError(
                f"Error inesperado durante la validación: {e}"
            ) from e

        else:
            # Se ejecuta solo si no hubo ninguna excepción
            log_info(f"Cliente '{self.nombre}' validado correctamente.")
            return True

        finally:
            # Se ejecuta siempre, haya o no excepción
            log_info(f"Proceso de validación del cliente '{self.nombre}' finalizado.")

    def mostrar_info(self) -> str:
        """
        Implementa el método abstracto de EntidadBase.
        Retorna una cadena con la información completa del cliente.

        Returns:
            str: Información formateada del cliente.
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
        """Representación en cadena del cliente."""
        return self.mostrar_info()
