from mongoengine import Document, StringField, EmbeddedDocumentField, FloatField, DateTimeField
from infrastructure.entities.color_entity import ColorEntity

class CalibrationEntity(Document):
    id = StringField(primary_key=True)
    reference_color = EmbeddedDocumentField(ColorEntity)
    detected_color = EmbeddedDocumentField(ColorEntity)
    deviation = FloatField()
    image_url = StringField()
    status = StringField(choices=["success", "failed", "needs_adjustment"])
    timestamp = DateTimeField()

    meta = {
        'collection': 'calibrations'
    }