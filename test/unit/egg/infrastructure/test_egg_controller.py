from app.controllers.egg_controller import EggController
from domain.models.egg_model import Egg

def test_create_egg_controller(mocker):
    controller = EggController()
    mock_use_case = mocker.patch.object(controller.create_egg_use_case, 'execute')
    
    fake_bytes = b"test"
    controller.create_egg(fake_bytes)
    
    mock_use_case.assert_called_once_with(fake_bytes)