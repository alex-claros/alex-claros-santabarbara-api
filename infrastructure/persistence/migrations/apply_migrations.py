import os
from importlib import import_module

def apply_migrations():
    """
    Aplica todas las migraciones disponibles en el directorio `migrations`.
    """
    print("Aplicando migraciones...")
    
    migrations_folder = os.path.dirname(__file__)
    for filename in sorted(os.listdir(migrations_folder)):
        if filename.startswith("0") and filename.endswith(".py"):
            module_name = filename[:-3]
            print(f"Ejecutando migración: {module_name}")
            migration_module = import_module(f"infrastructure.persistence.migrations.{module_name}")
            migration_module.run()
    
    print("Migraciones completadas.")