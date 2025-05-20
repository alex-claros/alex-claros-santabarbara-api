from unittest.mock import patch
from domain.models.egg_model import Egg
from infrastructure.entities.egg_entity import EggEntity
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

def test_save_egg():
    repo = EggRepositoryImpl()
    egg = Egg(
        position="1",
        viability=True,
        image_url="test.jpg",
        colorometry="#FFF",
        cracks=False,
        deformities=False,
        defects="none",
        confidence=0.95
    )
    
    with patch.object(EggEntity, 'save') as mock_save:
        repo.save(egg)
        mock_save.assert_called_once()

def test_find_non_viable_eggs():
    with patch.object(EggEntity, 'objects') as mock_objects:
        repo = EggRepositoryImpl()
        repo.find_non_viable_eggs()
        mock_objects.assert_called_with(viability=False)