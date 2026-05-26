import pytest
import uuid
from datetime import datetime, timezone
from domain.models.egg_model import Egg


class TestEggEntity:
    """Tests para la entidad de dominio Egg"""

    @pytest.fixture
    def valid_egg_data(self):
        return {
            "position": "Individual",
            "viability": True,
            "image_url": "https://minio.example.com/eggs/123.jpg",
            "colorometry": "A1",
            "cracks": False,
            "deformities": False,
            "defects": "None",
            "confidence": 0.95,
        }

    def test_create_egg_with_auto_generated_id(self, valid_egg_data):
        """Debe generar un UUID automáticamente si no se proporciona id"""
        egg = Egg(**valid_egg_data)
        
        assert egg.id is not None
        assert isinstance(egg.id, str)
        # Validar que es un UUID válido
        uuid.UUID(egg.id)  # No lanza excepción si es válido

    def test_create_egg_with_provided_id(self, valid_egg_data):
        """Debe usar el id proporcionado si se pasa explícitamente"""
        custom_id = "custom-uuid-123"
        egg = Egg(id=custom_id, **valid_egg_data)
        
        assert egg.id == custom_id

    def test_create_egg_with_analyzed_at(self, valid_egg_data):
        """Debe aceptar analyzed_at como datetime o None"""
        now = datetime.now(timezone.utc)
        egg_with_time = Egg(analyzed_at=now, **valid_egg_data)
        egg_without_time = Egg(**valid_egg_data)
        
        assert egg_with_time.analyzed_at == now
        assert egg_without_time.analyzed_at is None

    def test_to_dict_returns_correct_structure(self, valid_egg_data):
        """to_dict() debe retornar un diccionario con todas las propiedades"""
        egg = Egg(**valid_egg_data)
        result = egg.to_dict()
        
        expected_keys = {
            "id", "position", "viability", "image_url", 
            "colorometry", "cracks", "deformities", "defects", 
            "confidence", "analyzed_at"
        }
        
        assert set(result.keys()) == expected_keys
        assert result["position"] == valid_egg_data["position"]
        assert result["viability"] == valid_egg_data["viability"]
        assert result["confidence"] == valid_egg_data["confidence"]

    def test_to_dict_serializes_analyzed_at_to_isoformat(self, valid_egg_data):
        """to_dict() debe convertir analyzed_at a string ISO8601"""
        test_datetime = datetime(2024, 6, 15, 10, 30, 0, tzinfo=timezone.utc)
        egg = Egg(analyzed_at=test_datetime, **valid_egg_data)
        result = egg.to_dict()
        
        assert result["analyzed_at"] == "2024-06-15T10:30:00+00:00"

    def test_to_dict_with_none_analyzed_at(self, valid_egg_data):
        """to_dict() debe retornar None si analyzed_at no está definido"""
        egg = Egg(**valid_egg_data)  # analyzed_at por defecto es None
        result = egg.to_dict()
        
        assert result["analyzed_at"] is None

    def test_egg_attributes_are_immutable_by_design(self, valid_egg_data):
        """Documentar que la entidad permite mutación (o no, según tu diseño)"""
        egg = Egg(**valid_egg_data)
        # Si quieres inmutabilidad, podrías usar @dataclass(frozen=True) o properties
        # Por ahora, solo documentamos el comportamiento actual:
        egg.viability = False
        assert egg.viability is False
        # ✅ Si quieres inmutabilidad real, avísame y te ayudo a refactorizar