# SIGRES-APP
Sistema Integral de Gestion de Reservas, Clientes y Servicios
# SIGRES - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## 📌 Descripción
Sistema desarrollado como parte del Ejercicio 1 de la asignatura Programacion tarea 4
SIGRES-APP es una aplicación desarrollada en Python que implementa un sistema integral para la gestión de clientes, servicios y reservas de la empresa **Software FJ**.

El sistema está diseñado bajo los principios de la Programación Orientada a Objetos (POO) y NO utiliza bases de datos, gestionando la información mediante objetos, listas en memoria y archivos de registro (logs).

## 👥 Integrantes
- STEVEN EDUARDO GIL PADILLA
- CRISTIAN MAURICIO CELIS ARIAS
- GILMER DAVID CONDE LUNA
- Nombre 4
- Nombre 5

## 🛠️ Tecnologías utilizadas
- Python 3.13.12
- Sistema operativo: Windows / Linux / Mac

# 🧩 SIGRES-APP  
### Sistema Integral de Gestión de Clientes, Servicios y Reservas

## 🎯 Objetivo del Proyecto

Desarrollar un sistema:

- Modular y extensible
- Robusto ante errores
- Basado en POO (abstracción, herencia, encapsulación y polimorfismo)
- Con manejo avanzado de excepciones
- Capaz de continuar su ejecución incluso ante fallos

---

## 🧠 Principios Aplicados

- ✅ Abstracción (clases base)
- ✅ Encapsulación (datos protegidos en Cliente)
- ✅ Herencia (Servicios especializados)
- ✅ Polimorfismo (métodos sobrescritos)
- ✅ Manejo avanzado de excepciones

---

## 🏗️ Estructura del Proyecto
sigres-app/
│
├── main.py                          → Menú principal + 10 simulaciones
├── README.md
├── .gitignore
│
├── modelos/
│   ├── entidad_base.py              → Clase abstracta base
│   ├── cliente.py                   → Clase Cliente (encapsulada)
│   ├── servicio.py                  → Clase abstracta Servicio
│   └── reserva.py                   → Clase Reserva
│
├── servicios/
│   ├── reserva_sala.py              → Hereda de Servicio
│   ├── alquiler_equipo.py           → Hereda de Servicio
│   └── asesoria_especializada.py    → Hereda de Servicio
│
├── excepciones/
│   └── excepciones_personalizadas.py → Excepciones propias del sistema
│
├── utils/
│   └── logger.py                    → Registro de eventos y errores
│
└── logs/
    └── sigres.log

---

## ⚙️ Funcionalidades del Sistema

- Registro y validación de clientes
- Gestión de servicios (salas, equipos, asesorías)
- Creación y gestión de reservas
- Confirmación y cancelación de reservas
- Manejo de errores controlado
- Registro de eventos en archivo de logs
- Simulación de operaciones válidas e inválidas

---

## 🧪 Simulación del Sistema

El sistema ejecuta al menos **10 operaciones**, incluyendo:

- Registros de clientes válidos e inválidos
- Creación de servicios
- Reservas exitosas y fallidas
- Manejo de errores sin detener la ejecución

---

## 🚨 Manejo de Excepciones

El sistema incluye:

- Excepciones personalizadas
- Uso de:
  - `try / except`
  - `try / except / else`
  - `try / except / finally`
- Encadenamiento de excepciones
- Registro de errores en archivo `logs/sigres.log`

---

## 👥 Distribución del Equipo

### 🔹 David
- `servicio.py` → Clase abstracta Servicio
- `reserva_sala.py`
- `alquiler_equipo.py`
- `asesoria_especializada.py`

### 🔹 Cristian
- `cliente.py` → Encapsulación y validaciones
- `reserva.py` → Lógica de reservas y excepciones

### 🔹 Steven
- `entidad_base.py` → Clase abstracta base del sistema
- `excepciones_personalizadas.py` → Definición de excepciones
- `logger.py` → Registro de eventos y errores
- `main.py` → Ejecución, menú y simulaciones



## 🚀 Ejecución del Proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/GrupoUnad213023A2201/SIGRES-APP.git
cd SIGRES-APP