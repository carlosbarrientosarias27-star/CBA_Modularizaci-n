# CBA_Modularización

Organice los dos código (Biblioteca_1 y Tarea_2) en Python que nos dio el profesor separando responsabilidades en diferentes carpetas y archivos. 

# Biblioteca_1_app 


Ahora mismo tienes TODO en un solo archivo:

    - Modelo (Libro)

    - Lógica de negocio (Biblioteca)

    - Interfaz (menú)

    - Datos de prueba

Eso funciona… pero no escala 😅


## 🎯 Objetivo

Separar el código en:

    📦 Modelos → representan datos 

    ⚙️ Servicios / lógica → reglas del negocio

    🖥️ Interfaz → menú y entrada/salida

    🚀 Archivo principal → punto de entrada


## 📁 Estructura recomendada del proyecto 
```
biblioteca_app/
│
├── main.py
├── menu.py
│
├── models/
│   ├── __init__.py
│   └── libro.py
│
└── services/
    ├── __init__.py
    └── biblioteca.py 
    ´´´


# Tarea_2_app 


Ahora mismo tu código mezcla:

    - 📦 Datos

    - ✅ Validaciones

    - 🧠 Lógica

    - 🖥️ Interfaz (menú)

Vamos a dividirlo en módulos organizados por responsabilidad.


## 📁 Estructura propuesta del proyecto
```

│
├── main.py
├── models/
│   └── task_model.py
├── services/
│   └── task_service.py
└── utils/
    └── validators.py
    ´´´


## 🎯 Objetivo de cada módulo

| Archivo                    | Responsabilidad              |
| -------------------------- | ---------------------------- |
| `main.py`                  | Interfaz / Menú              |
| `models/task_model.py`     | Datos y estructura de tareas |
| `services/task_service.py` | Lógica del negocio           |
| `utils/validators.py`      | Validaciones                 |
