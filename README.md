# Indesap Tickets – API + SDK 

Microservicio demo de **gestión de tickets** desarrollado con **FastAPI**, acompañado de un **SDK en Python**.  
Proyecto creado como propuesta práctica para **Indesap**, mostrando buenas prácticas de desarrollo backend.

---

## 🚀 Características

- **API REST** con endpoints para:
  - Crear tickets
  - Listar tickets
  - Consultar ticket por ID
  - Cerrar tickets
- **SDK en Python** que facilita el consumo de la API.
- Validación de datos con **Pydantic** (ejemplo: título con mínimo 3 caracteres).
- **Documentación interactiva** en [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI).

---

## 📦 Requisitos

- Python 3.10+
- pip

---

## ▶️ Ejecutar la API

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
