from unittest.mock import MagicMock
from app.controllers.incubator_controller import IncubatorController
from domain.models.incubator_model import Incubator

def test_create_incubator():
    mock_repository = MagicMock()
    controller = IncubatorController()
    controller.create_incubator_use_case.repository = mock_repository

    incubator = Incubator(
        id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
        name="Incubadora Automática",
        capacity=150,
        status="activo",
        temperature="37.5 C",
        last_mant="2023-10-01",
        maples=[]
    )

    controller.create_incubator(incubator)
    mock_repository.save.assert_called_once_with(incubator)

def test_list_all_incubators():
    mock_repository = MagicMock()
    controller = IncubatorController()
    controller.list_all_incubators_use_case.repository = mock_repository

    mock_repository.find_all.return_value = [
        Incubator(
            id="f47ac10b-58cc-4372-a567-0e02b2c3d479",
            name="Incubadora Automática",
            capacity=150,
            status="activo",
            temperature="37.5 C",
            last_mant="2023-10-01",
            maples=[]
        )
    ]

    result = controller.list_all_incubators()
    assert len(result) == 1
    assert result[0].name == "Incubadora Automática"

def test_update_incubator():
    mock_repository = MagicMock()
    controller = IncubatorController()
    controller.update_incubator_use_case.repository = mock_repository

    updated_data = {"name": "Incubadora Actualizada"}
    controller.update_incubator("f47ac10b-58cc-4372-a567-0e02b2c3d479", updated_data)

    mock_repository.update.assert_called_once_with("f47ac10b-58cc-4372-a567-0e02b2c3d479", updated_data)

def test_soft_delete_incubator():
    mock_repository = MagicMock()
    controller = IncubatorController()
    controller.soft_delete_incubator_use_case.repository = mock_repository

    controller.soft_delete_incubator("f47ac10b-58cc-4372-a567-0e02b2c3d479")

    mock_repository.soft_delete.assert_called_once_with("f47ac10b-58cc-4372-a567-0e02b2c3d479")