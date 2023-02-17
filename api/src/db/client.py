import os
from urllib.parse import quote_plus

from pymongo import MongoClient

MONGO_HOST = os.getenv("MONGO_HOST", "db")
MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")

uri = "mongodb://%s:%s@%s" % (
    quote_plus(MONGO_USERNAME),
    quote_plus(MONGO_PASSWORD),
    MONGO_HOST,
)

connection = MongoClient(uri)
