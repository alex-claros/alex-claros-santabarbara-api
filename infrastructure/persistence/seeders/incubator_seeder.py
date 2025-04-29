from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepository
from datetime import datetime

def seed():
    """
    Carga datos iniciales para incubadoras.
    """
    print("Cargando datos iniciales para incubadoras...")
    
    data = [
        {
            "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
            "name": "Incubadora Automática",
            "capacity": 150,
            "status": "activo",
            "temperature": "37.5 C",
            "last_mant": "2023-10-01",
            "maples": [],
            "is_deleted": False,
            "deleted_at": None
        },
        {
            "id": "c9bf9e57-1685-4c89-bafb-ff5af830be8a",
            "name": "Incubadora Manual",
            "capacity": 100,
            "status": "mantenimiento",
            "temperature": "36.0 C",
            "last_mant": "2023-09-15",
            "maples": [],
            "is_deleted": True,
            "deleted_at": datetime(2023, 9, 20)
        }
    ]
    
    repository = IncubatorRepository()
    for item in data:
        repository.create_incubator(item)
    
    print("Datos de prueba cargados correctamente.")

if __name__ == "__main__":
    seed()