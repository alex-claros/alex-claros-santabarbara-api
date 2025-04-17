from fastapi import FastAPI
from app.controllers.endpoints.egg import eggs

app = FastAPI(
    title="Sistema de Detección de Huevos Inviables",
    description="API para detectar y gestionar la inviabilidad de huevos en un entorno de incubación.",
    version="1.0.0"
)

app.include_router(eggs.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
