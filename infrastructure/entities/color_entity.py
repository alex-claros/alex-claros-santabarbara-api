from mongoengine import EmbeddedDocument, IntField

class ColorEntity(EmbeddedDocument):
    r = IntField(required=True)
    g = IntField(required=True)
    b = IntField(required=True)