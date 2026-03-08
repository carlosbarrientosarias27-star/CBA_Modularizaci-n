# CBA_MODULARIZACION

Este repositorio contiene un conjunto de aplicaciones modulares desarrolladas en Python, diseñadas bajo una arquitectura de capas (Modelos, Servicios y Utilidades) para demostrar principios de organización de código y separación de responsabilidades.

## 📂 Estructura del Proyecto

El proyecto se divide en dos aplicaciones principales y herramientas de soporte:

### 1. Biblioteca_1_app
Sistema de gestión de libros y servicios bibliotecarios.
* **models/**: Define la estructura de datos (ej. `libro.py`).
* **services/**: Contiene la lógica de negocio (ej. `biblioteca.py`).
* **main.py / menu.py**: Puntos de entrada y manejo de la interfaz de usuario por consola.

### 2. Tareas_2_app
Gestor de tareas (To-Do list) con validaciones personalizadas.
* **models/**: Definición del objeto tarea (`task_model.py`).
* **services/**: Lógica para crear, listar o eliminar tareas (`task_service.py`).
* **utils/**: Funciones de apoyo y validaciones (`validators.py`).
* **main.py**: Ejecutor principal de la aplicación de tareas.

---

## 🚀 Cómo ejecutar las aplicaciones

Asegúrate de tener **Python 3.x** instalado en tu sistema.

### Ejecutar Biblioteca_1_app
1. Abre una terminal en la raíz del proyecto.
2. Navega a la carpeta de la aplicación:
   ```bash
   cd Biblioteca_1_app
