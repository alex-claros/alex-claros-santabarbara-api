import os
from importlib import import_module

def load_seeders():
    """
    Carga todos los seeders disponibles en el directorio `seeders`.
    """
    print("Cargando seeders...")
    
    seeders_folder = os.path.dirname(__file__)
    for filename in sorted(os.listdir(seeders_folder)):
        if filename.startswith("seeder_") and filename.endswith(".py"):
            module_name = filename[:-3]
            print(f"Ejecutando seeder: {module_name}")
            seeder_module = import_module(f"infrastructure.persistence.seeders.{module_name}")
            seeder_module.run()
    
    print("Seeders cargados correctamente.")