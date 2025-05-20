import pytest
from unittest.mock import MagicMock
from app.use_cases.egg.list_non_viable_eggs_use_case_impl import ListNonViableEggsUseCaseImpl
from domain.models.egg_model import Egg
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

@pytest.fixture
def mock_repository():
    return MagicMock(spec=EggRepositoryImpl)

@pytest.fixture
def sample_non_viable_eggs():
    return [
        Egg(
            id="1",
            position="1",
            viability=False,
            image_url="url1.jpg",
            colorometry="#000",
            cracks=True,
            deformities=True,
            defects="cracks",
            confidence=0.85
        ),
        Egg(
            id="2",
            position="2",
            viability=False,
            image_url="url2.jpg",
            colorometry="#111",
            cracks=False,
            deformities=True,
            defects="deformity",
            confidence=0.75
        )
    ]

def test_list_non_viable_eggs_use_case(mock_repository, sample_non_viable_eggs):
    # Arrange
    mock_repository.find_non_viable_eggs.return_value = sample_non_viable_eggs
    use_case = ListNonViableEggsUseCaseImpl(mock_repository)
    
    # Act
    result = use_case.execute()
    
    # Assert
    assert len(result) == 2
    assert all(not egg.viability for egg in result)
    mock_repository.find_non_viable_eggs.assert_called_once()