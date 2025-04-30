import pytest
from datetime import datetime
from infrastructure.persistence.repositories.incubator_repository_impl import IncubatorRepositoryImpl
from domain.models.incubator_model import Incubator
from infrastructure.entities.incubator_entity import IncubatorEntity

@pytest.fixture
def mock_mongo():
    from mongoengine import connect, disconnect
    connect("test_db", host="mongomock://localhost")
    yield
    disconnect()

def test_save_incubator(mock_mongo):
    repository = IncubatorRepositoryImpl()
    incubator = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )
    repository.save(incubator)

    saved_incubator = IncubatorEntity.objects(id="f47ac10b-58cc-4372-a567-0e02b2c3d479").first()
    assert saved_incubator.name == "Incubadora Automática"
    assert saved_incubator.capacity == 150

def test_find_all(mock_mongo):
    repository = IncubatorRepositoryImpl()

    incubator1 = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )
    incubator2 = Incubator(
        id="c9bf9e57-1685-4c89-bafb-ff5af830be8a",
        name="Incubadora Manual",
        capacity=100,
        status="mantenimiento",
        temperature="36.0 C",
        last_mant="2023-09-15",
        maples=[]
    )
    repository.save(incubator1)
    repository.save(incubator2)

    result = repository.find_all()
    assert len(result) == 2
    assert result[0].name == "Incubadora Automática"
    assert result[1].name == "Incubadora Manual"

def test_find_by_id(mock_mongo):
    repository = IncubatorRepositoryImpl()

    incubator = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )
    repository.save(incubator)

    result = repository.find_by_id("f47ac10b-58cc-4372-a567-0e02b2c3d479")
    assert result.id == "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    assert result.name == "Incubadora Automática"

def test_update_incubator(mock_mongo):
    repository = IncubatorRepositoryImpl()

    incubator = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )
    repository.save(incubator)

    updated_data = {"name": "Incubadora Actualizada"}
    repository.update("f47ac10b-58cc-4372-a567-0e02b2c3d479", updated_data)

    updated_incubator = repository.find_by_id("f47ac10b-58cc-4372-a567-0e02b2c3d479")
    assert updated_incubator.name == "Incubadora Actualizada"

def test_soft_delete(mock_mongo):
    repository = IncubatorRepositoryImpl()

    incubator = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )
    repository.save(incubator)

    repository.soft_delete("f47ac10b-58cc-4372-a567-0e02b2c3d479")

    deleted_incubator = IncubatorEntity.objects(id="f47ac10b-58cc-4372-a567-0e02b2c3d479").first()
    assert deleted_incubator.is_deleted is True
    assert deleted_incubator.deleted_at is not None