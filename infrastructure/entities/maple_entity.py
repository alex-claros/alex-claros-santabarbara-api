from mongoengine import Document, StringField, IntField, ListField, ReferenceField, BooleanField, DateTimeField
from domain.models.maple_model import Maple
from infrastructure.entities.egg_entity import EggEntity

class MapleEntity(Document):
    id = StringField(primary_key=True)
    name = StringField(required=True)
    capacity = IntField(required=True)
    status = StringField(default="Disponible")
    level = StringField(required=False)
    eggs = ListField(ReferenceField("EggEntity"))
    load_date = DateTimeField(null=True)
    responsible = StringField(required=False)
    is_deleted = BooleanField(default=False)
    deleted_at = DateTimeField(null=True)

    def to_domain_model(self):
        from infrastructure.entities.egg_entity import EggEntity
        return Maple(
            id=str(self.id),
            name=self.name,
            capacity=self.capacity,
            status=self.status,
            level=self.level,
            eggs=[e.to_domain_model() for e in self.eggs],
            load_date=self.load_date,
            responsible=self.responsible,
            is_deleted=self.is_deleted,
            deleted_at=self.deleted_at
        )

    @staticmethod
    def from_domain_model(maple: Maple):
        return MapleEntity(
            id=maple.id,
            name=maple.name,
            capacity=maple.capacity,
            status=maple.status,
            level=maple.level,
            eggs=[EggEntity.from_domain_model(e) for e in maple.eggs],
            load_date=maple.load_date,
            is_deleted=maple.is_deleted,
            deleted_at=maple.deleted_at
        )