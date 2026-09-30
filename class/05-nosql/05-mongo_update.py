#!/usr/bin/env python3
"""Update documents in mypractice.fruit with $set."""
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

log.info("Before update:")
get_record = fruit.find({"name": "apple"})
log.info("%s", dumps(list(get_record), indent=2))

log.info("Updating apple quantity to 8 and restocked to True:")
fruit.update_one({"name": "apple"}, {"$set": {"quantity": 8}})
fruit.update_one({"name": "apple"}, {"$set": {"restocked": True}})

# Full list of MongoDB operators: https://www.mongodb.com/docs/manual/reference/operator/

log.info("After update:")
get_record = fruit.find({"name": "apple"})
log.info("%s", dumps(list(get_record), indent=2))

client.close()
