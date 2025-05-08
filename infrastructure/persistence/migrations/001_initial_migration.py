from mongoengine import connect, disconnect
from infrastructure.entities.incubator_entity import IncubatorEntity

def run():
    """
    Configura la estructura inicial de la base de datos.
    """
    print("Ejecutando migración inicial...")
    
    # Conectar a MongoDB
    connect("egg_detection_db", host="mongodb://root:example@egg_detection_mongo:2709")
    
    # Crear índices
    IncubatorEntity.create_index("id", unique=True)
    IncubatorEntity.create_index("name")
    
    print("Migración inicial completada.")
    
    # Desconectar
    disconnect()