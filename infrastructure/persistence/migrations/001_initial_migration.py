from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepository

def migrate():
    """
    Aplicación de la migración inicial.
    """
    print("Aplicando migración inicial...")

    repository = IncubatorRepository()
    repository.create_initial_collections()

if __name__ == "__main__":
    migrate()