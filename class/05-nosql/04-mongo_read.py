#!/usr/bin/env python3
"""Read documents from mypractice.fruit."""
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

get_one = fruit.find_one()
log.info("One document: %s", dumps(get_one, indent=2))

get_another = fruit.find({"name": "apple"})
log.info("%s", dumps(list(get_another), indent=2))

get_more = fruit.count_documents({"quantity": {"$gte": 5}})
log.info("%s fruit with quantity >= 5", get_more)

client.close()
