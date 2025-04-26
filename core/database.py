from mongoengine import connect

def init_db():
    connect(
        db="egg_viability_db",
        host="mongodb://root:example@localhost:27017",
        alias="default"
    )