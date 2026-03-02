# CBA_Modularización

Organice los dos código (Biblioteca_1 y Tarea_2) en Python que nos dio el profesor separando responsabilidades en diferentes carpetas y archivos. 


# Tareas_2_app 


Ahora mismo tu código mezcla:

    - 📦 Datos

    - ✅ Validaciones

    - 🧠 Lógica

    - 🖥️ Interfaz (menú)

Vamos a dividirlo en módulos organizados por responsabilidad.


## 📁 Estructura propuesta del proyecto
```
Tareas_2_app/
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
