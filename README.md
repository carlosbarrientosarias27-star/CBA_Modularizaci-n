# 📚 Proyectos Python — Documentación Unificada

Este repositorio documenta dos proyectos Python que evolucionan desde una estructura simple hacia una arquitectura modular profesional.

---

# 📁 Proyecto de Prueba

Proyecto inicial con estructura básica y plana. Sirve como punto de partida para explorar los conceptos fundamentales antes de aplicar una arquitectura modularizada.

## Estructura

```
Proyecto de Prueba/
├── __init__.py          # Inicialización del paquete
├── biblioteca_1.py      # Módulo de gestión de biblioteca
├── tareas_2.py          # Módulo de gestión de tareas
└── readme.md            # Documentación del proyecto
```

## Descripción de archivos

| Archivo | Descripción |
|---|---|
| `__init__.py` | Marca el directorio como paquete Python |
| `biblioteca_1.py` | Lógica relacionada con la gestión de libros/biblioteca |
| `tareas_2.py` | Lógica relacionada con la gestión de tareas |

## Características
- Estructura sencilla y directa
- Todo el código en el directorio raíz
- Ideal para prototipos y aprendizaje inicial

---

# 📦 Proyecto Modularización

Versión evolucionada que aplica principios de **arquitectura en capas** (models / services / utils), separando responsabilidades en dos aplicaciones independientes.

## Estructura

```
Proyecto Modularización/
├── Biblioteca_1_app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── libro.py             # Modelo de datos del libro
│   ├── services/
│   │   ├── __init__.py
│   │   └── biblioteca.py        # Lógica de negocio de biblioteca
│   ├── main.py                  # Punto de entrada de la app
│   └── menu.py                  # Interfaz de menú para el usuario
│
├── Tareas_2_app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── task_model.py        # Modelo de datos de tarea
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Lógica de negocio de tareas
│   └── utils/
│       ├── __init__.py
│       └── validators.py        # Utilidades de validación
│
├── __init__.py
├── main.py                      # Punto de entrada principal
├── LICENSE
└── README.md
```

# Descripción por capa

## 🏗️ Models (Modelos)
Contienen las estructuras de datos (clases/entidades) del dominio.

| Archivo | Descripción |
|---|---|
| `Biblioteca_1_app/models/libro.py` | Define la clase `Libro` con sus atributos |
| `Tareas_2_app/models/task_model.py` | Define la clase `Task` con sus atributos |

## ⚙️ Services (Servicios)
Contienen la lógica de negocio y las operaciones sobre los modelos.

| Archivo | Descripción |
|---|---|
| `Biblioteca_1_app/services/biblioteca.py` | CRUD y operaciones sobre libros |
| `Tareas_2_app/services/task_service.py` | CRUD y operaciones sobre tareas |

## 🛠️ Utils (Utilidades)
Funciones auxiliares reutilizables, independientes del dominio.

| Archivo | Descripción |
|---|---|
| `Tareas_2_app/utils/validators.py` | Validaciones de entrada de datos |

# Características
- Separación clara de responsabilidades (SoC)
- Arquitectura escalable y mantenible
- Reutilización de código mediante capas
- Fácil incorporación de pruebas unitarias por capa

---

## 🔄 Comparativa entre proyectos

| Aspecto | Proyecto de Prueba | Proyecto Modularización |
|---|---|---|
| **Estructura** | Plana (un solo nivel) | Jerárquica por capas |
| **Escalabilidad** | Limitada | Alta |
| **Separación de responsabilidades** | No | Sí (models / services / utils) |
| **Mantenibilidad** | Básica | Profesional |
| **Ideal para** | Prototipos, aprendizaje | Proyectos en producción |

---

# 🚀 Cómo ejecutar

## Proyecto de Prueba
```
cd "Proyecto de Prueba"
python biblioteca_1.py
python tareas_2.py
```

## Proyecto Modularización
```
cd "Proyecto Modularización"
python main.py
```

---

# 🛠️ Requisitos

- Python 3.14
- No se requieren dependencias externas

---

# 📄 Licencia

Este proyecto está bajo los términos de la licencia incluida en el archivo `LICENSE` MIT.
