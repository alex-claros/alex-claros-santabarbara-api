from mongoengine import Document, StringField, IntField, BooleanField, FloatField, DateTimeField
from domain.models.egg_model import Egg

class EggEntity(Document):
    id = StringField(primary_key=True)  # ID único del huevo
    position = StringField()  # Posición dentro del maple
    viability = BooleanField()  # Viabilidad del huevo (True o False)
    image_url = StringField()  # URL de la imagen almacenada en MinIO
    colorometry = StringField()  # Valor de colorimetría
    cracks = BooleanField()  # Indica si tiene grietas
    deformities = BooleanField()  # Indica si tiene deformidades
    defects = StringField()  # Indica si tiene defectos estructurales
    confidence = FloatField()  # Referencia al maple al que pertenece
    analyzed_at = DateTimeField() 

    def to_domain_model(self):
        return Egg(
            id=str(self.id),
            position=self.position,
            viability=self.viability,
            image_url=self.image_url,
            colorometry=self.colorometry,
            cracks=self.cracks,
            deformities=self.deformities,
            defects=self.defects,
            confidence=self.confidence,
            analyzed_at=self.analyzed_at, 
        )
    
    @staticmethod
    def from_domain_model(egg: Egg):
        return EggEntity(
            id=egg.id,
            position=egg.position,
            viability=egg.viability,
            image_url=egg.image_url,
            colorometry=egg.colorometry,
            cracks=egg.cracks,
            deformities=egg.deformities,
            defects=egg.defects,
            confidence=egg.confidence,
            analyzed_at=egg.analyzed_at
        )