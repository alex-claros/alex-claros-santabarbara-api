from mongoengine import Document, StringField, ReferenceField, ListField

class MapleEntity(Document):
    id = StringField(primary_key=True)  # ID único del maple
    incubator = ReferenceField("Incubator")  # Referencia a la incubadora
    eggs = ListField(ReferenceField("Egg"))  # Lista de huevos en el maple