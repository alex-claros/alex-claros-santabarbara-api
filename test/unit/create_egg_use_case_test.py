import pytest
from unittest.mock import MagicMock, patch
from domain.models.egg_model import Egg
from app.use_cases.egg.create_egg_use_case_impl import CreateEggUseCaseImpl
from app.services.roboflow_service import RoboflowService
from core.minio_client import MinioClient
from infrastructure.persistence.repositories.egg_repository_impl import EggRepositoryImpl

@pytest.fixture
def mock_repository():
    return MagicMock(spec=EggRepositoryImpl)

@pytest.fixture
def mock_roboflow():
    return MagicMock(spec=RoboflowService)

@pytest.fixture
def mock_minio():
    return MagicMock(spec=MinioClient)

@pytest.fixture
def use_case(mock_repository, mock_roboflow):
    return CreateEggUseCaseImpl(repository=mock_repository, roboflow_service=mock_roboflow)

@pytest.fixture
def fake_image_bytes():
    return b"fake_image_content"

@pytest.fixture
def roboflow_response():
    return {
        "predictions": [
            {
                "class": "Healty",
                "confidence": 0.95,
                "x": 100,
                "y": 200,
                "width": 50,
                "height": 60
            }
        ]
    }

def test_execute_success(use_case, mock_repository, mock_roboflow, mock_minio, fake_image_bytes, roboflow_response):
    # Mock MinIO
    with patch.object(use_case, 'minio_client', mock_minio):
        mock_minio.upload_image.return_value = "https://minio.example.com/eggs/123.jpg "
        
        # Mock Roboflow
        mock_roboflow.analyze_image.return_value = roboflow_response
        
        # Ejecutar
        result = use_case.execute(fake_image_bytes)
        
        # Verificaciones
        mock_minio.upload_image.assert_called_once_with(fake_image_bytes)
        mock_roboflow.analyze_image.assert_called_once_with(fake_image_bytes)
        mock_repository.save.assert_called_once()
        
        # Validar salida
        assert len(result) == 1
        egg_dict = result[0]
        assert egg_dict["position"] == "Individual"
        assert egg_dict["viability"] is True
        assert egg_dict["cracks"] is False
        assert egg_dict["image_url"] == "https://minio.example.com/eggs/123.jpg "

def test_execute_no_predictions(use_case, mock_repository, mock_roboflow, mock_minio, fake_image_bytes):
    # Mock sin detecciones
    mock_roboflow.analyze_image.return_value = {"predictions": []}
    
    # Ejecutar
    result = use_case.execute(fake_image_bytes)
    
    # Verificar
    assert result == []
    mock_repository.save.assert_not_called()

def test_execute_multiple_eggs(use_case, mock_repository, mock_roboflow, mock_minio, fake_image_bytes):
    # Mock con múltiples huevos
    mock_roboflow.analyze_image.return_value = {
        "predictions": [
            {"class": "Healty", "confidence": 0.9, "x": 10, "y": 20},
            {"class": "Damage", "confidence": 0.85, "x": 30, "y": 40}
        ]
    }
    
    # Ejecutar
    result = use_case.execute(fake_image_bytes)
    
    # Verificar
    assert len(result) == 2
    assert result[0]["viability"] is True
    assert result[0]["position"] == "Individual"
    assert result[1]["viability"] is False
    assert result[1]["cracks"] is True
    assert mock_repository.save.call_count == 2

def test_execute_invalid_image(use_case, mock_roboflow, fake_image_bytes):
    # Mock error en Roboflow
    mock_roboflow.analyze_image.side_effect = Exception("Invalid image")
    
    with pytest.raises(Exception):
        use_case.execute(fake_image_bytes)