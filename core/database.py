from mongoengine import connect

def init_db():
    connect(
        db="egg_detection_db",
        host="mongodb://db:27017/",
        alias="default"
    )