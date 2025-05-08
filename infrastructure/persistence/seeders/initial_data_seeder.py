from mongoengine import connect, disconnect
from infrastructure.entities.incubator_entity import IncubatorEntity

def run():
    """
    Carga datos iniciales en la base de datos.
    """
    print("Cargando datos iniciales...")
    
    connect("egg_detection_db", host="mongodb://root:example@egg_detection_mongo:27017")
    
    if IncubatorEntity.objects.count() > 0:
        print("Los datos iniciales ya existen. No se cargarán nuevamente.")
        return
    
    initial_incubators = [
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
            "is_deleted": False,
            "deleted_at": None
        }
    ]
    
    for data in initial_incubators:
        incubator = IncubatorEntity(**data)
        incubator.save()
    
    print("Datos iniciales cargados correctamente.")
    
    disconnect()