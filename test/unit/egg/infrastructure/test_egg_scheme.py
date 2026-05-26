import pytest
from datetime import datetime
from pydantic import ValidationError
from infrastructure.schemas.egg_schema import EggSchema


class TestEggSchema:
    def test_create_valid_schema(self):
        data = {
            "position": "Individual",
            "viability": True,
            "image_url": "https://example.com/egg.jpg",
            "colorometry": "A1",
            "cracks": False,
            "deformities": False,
            "defects": "None",
            "confidence": 0.95,
            "analyzed_at": datetime.now(),
        }
        schema = EggSchema(**data)
        assert schema.position == "Individual"

    def test_schema_requires_all_fields(self):
        with pytest.raises(ValidationError):
            EggSchema(position="Individual")