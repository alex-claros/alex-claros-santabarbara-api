from mongoengine import Document, StringField, IntField, BooleanField, FloatField, ReferenceField

class EggEntity(Document):
    id = StringField(primary_key=True)  # ID único del huevo
    position = IntField()  # Posición dentro del maple
    viability = BooleanField()  # Viabilidad del huevo (True o False)
    image_url = StringField()  # URL de la imagen almacenada en MinIO
    colorimetry = FloatField()  # Valor de colorimetría
    structural_defects = BooleanField()  # Indica si tiene defectos estructurales
    maple = ReferenceField("Maple")  # Referencia al maple al que pertenece