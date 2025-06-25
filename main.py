from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.database import init_db
from app.routes.egg_route import router as egg_router
from app.routes.maple_route import router as maple_router
from app.routes.incubator_route import router as incubator_router
from app.routes.calibration_route import router as calibration_router

app = FastAPI()

origins = [
    "http://localhost:3000",  # frontend en desarrollo
    "http://127.0.0.1:3000",  # Otra forma común de acceder localmente
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Orígenes permitidos
    allow_credentials=True,      # Permitir credenciales
    allow_methods=["*"],         # Permitir todos los métodos HTTP
    allow_headers=["*"],         # Permitir todos los encabezados
)

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(egg_router, prefix="/api", tags=["Eggs"])
app.include_router(maple_router, prefix="/api", tags=["Maples"])
app.include_router(incubator_router, prefix="/api", tags=["Incubators"])
app.include_router(calibration_router, prefix="/api", tags=["Calibration"])