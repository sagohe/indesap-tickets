from __future__ import annotations
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from .routes.tickets import router as tickets_router
from pathlib import Path

# Desplegamos Indesap Tickets API
# Incluimos todos los endpoints (rutas)

app = FastAPI(
    title="Gestion de Tickets",
    version="0.1.0",
    docs_url="/docs",          # fuerza Swagger en /docs 
    openapi_url="/openapi.json"  # fuerza el esquema en /openapi.json
)

app.include_router(tickets_router)

# Ruta al directorio frontend (../frontend desde app/main.py)
frontend_dir = Path(__file__).resolve().parent.parent / "frontend"

# Monta los archivos estáticos en /web (servirá index.html por defecto)
app.mount("/web", StaticFiles(directory=frontend_dir, html=True), name="web")

@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Gestion de Tickets", "docs": "/docs", "health": "/health"}

# Ver si la API esta viva

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
