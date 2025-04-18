from mongoengine import Document, StringField, IntField, ListField, ReferenceField

class Incubator(Document):
    id = StringField(primary_key=True)  # ID único de la incubadora
    name = str # Nombre reconocible de la incubadora
    capacity = IntField()  # Capacidad máxima de maples
    temperature = str # Temperatura ideal de la incubadora
    last_mant = str # Ultima vez que se realizo mantenimiento
    maples = ListField(ReferenceField("Maple"))  # Lista de maples en la incubadora