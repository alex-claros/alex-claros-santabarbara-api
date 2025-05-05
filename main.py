from fastapi import FastAPI
from core.database import init_db
from app.routes.egg_route import router as egg_router
from app.routes.maple_route import router as maple_router
from app.routes.incubator_route import router as incubator_router

app = FastAPI()

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(egg_router, prefix="/api/eggs", tags=["Eggs"])
app.include_router(maple_router, prefix="/api", tags=["Maples"])
app.include_router(incubator_router, prefix="/api", tags=["Incubators"])