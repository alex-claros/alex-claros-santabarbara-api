import pytest
from unittest.mock import MagicMock
from domain.models.egg_model import Egg
from app.use_cases.egg.list_all_eggs_use_case_impl import ListAllEggsUseCaseImpl
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

@pytest.fixture
def mock_repository():
    return MagicMock(spec=EggRepositoryImpl)

@pytest.fixture
def sample_eggs():
    return [
        Egg(
            id="1",
            position="1",
            viability=True,
            image_url="url1.jpg",
            colorometry="#FFF",
            cracks=False,
            deformities=False,
            defects="none",
            confidence=0.95
        ),
        Egg(
            id="2",
            position="2",
            viability=False,
            image_url="url2.jpg",
            colorometry="#000",
            cracks=True,
            deformities=True,
            defects="cracks",
            confidence=0.85
        )
    ]

def test_list_all_eggs_use_case(mock_repository, sample_eggs):
    # Arrange
    mock_repository.find_all.return_value = sample_eggs
    use_case = ListAllEggsUseCaseImpl(mock_repository)
    
    # Act
    result = use_case.execute()
    
    # Assert
    assert len(result) == 2
    assert result[0].id == "1"
    assert result[1].defects == "cracks"
    mock_repository.find_all.assert_called_once()