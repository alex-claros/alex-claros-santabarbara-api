from mongoengine import Document, StringField, IntField, ListField, ReferenceField, BooleanField, DateTimeField
from domain.models.incubator_model import Incubator
from infrastructure.entities.maple_entity import MapleEntity 

class IncubatorEntity(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    capacity = IntField(required=True)
    status = StringField(default="Disponible")
    temperature = StringField(default="37.5°C")
    last_mant = StringField(default="N/A")
    maples = ListField(ReferenceField("MapleEntity"))
    is_deleted = BooleanField(default=False)
    deleted_at = DateTimeField(null=True)

    def to_domain_model(self):
        from infrastructure.entities.maple_entity import MapleEntity
        return Incubator(
            id=str(self.id),
            name=self.name,
            capacity=self.capacity,
            status=self.status,
            temperature=self.temperature,
            last_mant=self.last_mant,
            maples=[m.to_domain_model() for m in self.maples],
            is_deleted=self.is_deleted,
            deleted_at=self.deleted_at
        )

    @staticmethod
    def from_domain_model(incubator: Incubator):
        return IncubatorEntity(
            id=incubator.id,
            name=incubator.name,
            capacity=incubator.capacity,
            status=incubator.status,
            temperature=incubator.temperature,
            last_mant=incubator.last_mant,
            maples=[MapleEntity.from_domain_model(m) for m in incubator.maples],
            is_deleted=incubator.is_deleted,
            deleted_at=incubator.deleted_at
        )