from mongoengine import Document, StringField, IntField, BooleanField, FloatField
from domain.models.egg_model import Egg

class EggEntity(Document):
    id = StringField(primary_key=True)  # ID único del huevo
    position = IntField()  # Posición dentro del maple
    viability = BooleanField()  # Viabilidad del huevo (True o False)
    image_url = StringField()  # URL de la imagen almacenada en MinIO
    colorimetry = FloatField()  # Valor de colorimetría
    defects = StringField()  # Indica si tiene defectos estructurales
    confidence = FloatField()  # Referencia al maple al que pertenece

    def to_domain_model(self):
        return Egg(
            id=str(self.id),
            position=self.position,
            viability=self.viability,
            image_url=self.image_url,
            colorometry=self.colorimetry,
            defects=self.defects,
            confidence=self.confidence,
        )
    
    @staticmethod
    def from_domain_model(egg: Egg):
        return EggEntity(
            id=egg.id,
            position=egg.position,
            viability=egg.viability,
            image_url=egg.image_url,
            colorometry=egg.colorometry,
            defect=egg.defects,
            confidence=egg.confidence
        )