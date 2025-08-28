# Indesap Tickets – API + SDK + CI

![CI](https://github.com/<TU-USUARIO>/<TU-REPO>/actions/workflows/ci.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)

Microservicio demo de **gestión de tickets** desarrollado con **FastAPI**, acompañado de un **SDK en Python** y un pipeline completo de **CI/CD** con GitHub Actions.  
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
- **CI/CD con GitHub Actions**:
  - Ruff → lint y orden de imports
  - Black → formato consistente
  - Mypy → tipado estático
  - Pytest → pruebas unitarias
  - Coverage → reporte de cobertura
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
