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
biblioteca_1_app/
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

🧠 Concepto Clave: Separación de Responsabilidades

Cada módulo tiene UNA tarea: 

| Módulo        | Responsabilidad      |
| ------------- | -------------------- |
| libro.py      | Representar datos    |
| biblioteca.py | Lógica del negocio   |
| menu.py       | Interfaz             |
| main.py       | Arranque del sistema |
