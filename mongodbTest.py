from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://10.2.2.2:27017/')
db = client.odin
partners = db.partners
pprint.pprint(partners.find_one())
