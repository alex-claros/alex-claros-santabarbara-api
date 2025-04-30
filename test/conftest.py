import pytest
from mongoengine import connect, disconnect
from mongomock import MongoClient

@pytest.fixture(scope="function")
def mock_mongo():
    connect("test_db", host="mongomock://localhost")
    yield
    disconnect()