import pytest
from datetime import datetime
from domain.models.incubator_model import Incubator

def test_incubator_initialization():
    incubator_data = {
        "id": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
        "name": "Incubadora Automática",
        "capacity": 150,
        "status": "activo",
        "temperature": "37.5 C",
        "last_mant": "2023-10-01",
        "maples": [],
        "is_deleted": False,
        "deleted_at": None
    }

    incubator = Incubator(**incubator_data)

    assert incubator.id == "f47ac10b-58cc-4372-a567-0e02b2c3d479"
    assert incubator.name == "Incubadora Automática"
    assert incubator.capacity == 150
    assert incubator.is_deleted is False
    assert incubator.deleted_at is None

def test_incubator_default_values():
    incubator = Incubator(
        name="Incubadora Manual",
        capacity=100,
        status="mantenimiento",
        temperature="36.0 C",
        last_mant="2023-09-15",
        maples=[]
    )

    assert incubator.is_deleted is False
    assert incubator.deleted_at is None