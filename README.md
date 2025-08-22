# Indesap Tickets – API + SDK + CI


Demo enfocada en Indesap: microservicio FastAPI de **gestión de tickets** + **SDK Python** + **pipeline** (lint, types, tests, coverage).


## Ejecutar API
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

git remote add origin https://github.com/sagohe/indesap.git
git branch -M main
git push -u origin main