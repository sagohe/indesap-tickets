from __future__ import annotations

from fastapi import FastAPI
from .routes.tickets import router as tickets_router

# Desplegamos Indesap Tickets API
# Incluimos todos los endpoints (rutas)

app = FastAPI(
    title="Indesap Tickets API",
    version="0.1.0",
    docs_url="/docs",          # fuerza Swagger en /docs 
    openapi_url="/openapi.json"  # fuerza el esquema en /openapi.json
)

app.include_router(tickets_router)


@app.get("/")
def root() -> dict[str, str]:
    return {"message": "Indesap Tickets API", "docs": "/docs", "health": "/health"}

# Ver si la API esta viva

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
