import pytest
from unittest.mock import MagicMock
from domain.repositories.egg_repository import EggRepository
from app.services.roboflow_service import RoboflowService
from core.minio_client import MinioClient

@pytest.fixture
def mock_repository():
    return MagicMock(spec=EggRepository)

@pytest.fixture
def mock_roboflow():
    return MagicMock(spec=RoboflowService)

@pytest.fixture
def mock_minio():
    return MagicMock(spec=MinioClient)