# 📦 Proyecto Modularización

Proyecto Python estructurado con arquitectura modular, separando responsabilidades en aplicaciones independientes que siguen el patrón de capas **models / services / utils**.

---

# 🗂️ Estructura del Proyecto

```
Proyecto Modularización/
│
├── Biblioteca_1_app/               # Módulo de gestión de biblioteca
│   ├── models/
│   │   ├── __init__.py
│   │   └── libro.py                # Modelo de datos: Libro
│   ├── services/
│   │   ├── __init__.py
│   │   └── biblioteca.py          # Lógica de negocio de la biblioteca
│   ├── main.py                     # Punto de entrada de la app Biblioteca
│   └── menu.py                     # Menú interactivo de la app Biblioteca
│
├── Tareas_2_app/                   # Módulo de gestión de tareas
│   ├── models/
│   │   ├── __init__.py
│   │   └── task_model.py          # Modelo de datos: Tarea
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py        # Lógica de negocio de tareas
│   └── utils/
│       ├── __init__.py
│       └── validators.py          # Validadores y utilidades compartidas
│
├── __init__.py
├── main.py                         # Punto de entrada principal del proyecto
├── LICENSE
└── README.md
```

---

# 🧩 Módulos

## 📚 Biblioteca_1_app

Aplicación encargada de gestionar una biblioteca de libros.

| Archivo | Descripción |
|---|---|
| `models/libro.py` | Define la clase `Libro` con sus atributos y métodos |
| `services/biblioteca.py` | Contiene la lógica para agregar, listar, buscar y eliminar libros |
| `main.py` | Inicializa y arranca la aplicación de biblioteca |
| `menu.py` | Gestiona el menú de interacción con el usuario |

---

## ✅ Tareas_2_app

Aplicación encargada de gestionar una lista de tareas.

| Archivo | Descripción |
|---|---|
| `models/task_model.py` | Define la clase `Task` con sus atributos y métodos |
| `services/task_service.py` | Contiene la lógica para crear, completar, listar y eliminar tareas |
| `utils/validators.py` | Funciones de validación reutilizables entre módulos |

---

# 🚀 Instalación y Uso

## Prerrequisitos

- Python 3.14

## Clonar el repositorio

```
git clone https://github.com/tu-usuario/proyecto-modularizacion.git
cd proyecto-modularizacion
```

# Ejecutar el proyecto

```
python main.py
```

O ejecutar cada aplicación de forma independiente:

```
# Aplicación Biblioteca
python Biblioteca_1_app/main.py

# Aplicación Tareas
python Tareas_2_app/main.py  # (si dispone de su propio punto de entrada)
```

---

# 🏗️ Arquitectura

El proyecto sigue una **arquitectura en capas** por módulo:

```
┌─────────────────────────────┐
│          main.py / menu      │  ← Capa de presentación (UI/CLI)
├─────────────────────────────┤
│           services/          │  ← Capa de lógica de negocio
├─────────────────────────────┤
│            models/           │  ← Capa de datos / entidades
├─────────────────────────────┤
│             utils/           │  ← Utilidades y validadores transversales
└─────────────────────────────┘
```

Cada aplicación (`Biblioteca_1_app`, `Tareas_2_app`) es **independiente** y puede extenderse o reemplazarse sin afectar al resto del sistema.

---

# 📄 Licencia

Este proyecto está licenciado bajo los términos del archivo [LICENSE](./LICENSE MIT).