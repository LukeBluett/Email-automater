import pymongo
from pymongo import MongoClient

class DBHandler:
	def __init__(self, ip_address, port_no, database, collection):
		try:
			self.__client = MongoClient(ip_address, port_no)
			self.__database = self.__client[database]
			self.__collection = db[collection]
		except exception:
			print("Error: Failed connecting to database")

	def create(self, post):
		return self.__collection.insert_one(post).inserted_id

	def find(self, search_object, search_query):
		return self.__collection.find_one({search_object: search_query})

	def update(self, mongo_id, post):
		self.__collection.update_one({'_id': mongo_id}, {"$set":post})

	def delete(self, mongo_id):
		self.__collection.remove({'_id': mongo_id})

