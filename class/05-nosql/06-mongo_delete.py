#!/usr/bin/env python3
"""Delete documents from mypractice.fruit."""
import logging
import os

from bson.json_util import dumps
from pymongo import MongoClient

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)

uri = os.getenv("MONGODB_ATLAS_URL")
username = os.getenv("MONGODB_ATLAS_USER")
password = os.getenv("MONGODB_ATLAS_PWD")

client = MongoClient(uri, username=username, password=password, connectTimeoutMS=200, retryWrites=True)
db = client.mypractice
fruit = db.fruit

get_record = fruit.find({"name": "apple"})
log.info("Documents matching name 'apple': %s", dumps(list(get_record), indent=2))

fruit.delete_one({"name": "apple"})

get_record = fruit.find({})
log.info("All documents after delete: %s", dumps(list(get_record), indent=2))

# To delete all documents matching a filter: fruit.delete_many({"name": "orange"})

client.close()
