import pymongo
from pymongo import MongoClient
import my_email
from my_email import *

class DBHandler:
	def __init__(self, ip_address, port_no, database):
		try:
			self.__client = MongoClient(ip_address, port_no)
			self.__db = self.__client[database]
			self.__employees = self.__db.employees
			self.__jobs = self.__db.jobs
		except:
			print("Error: Failed connecting to database")

	def create(self, post):
		return self.__collection.insert_one(post).inserted_id

	def find(self, search_object, search_query):
		return self.__collection.find_one({search_object: search_query})

	def update(self, mongo_id, post):
		self.__collection.update_one({'_id': mongo_id}, {"$set":post})

	def delete(self, mongo_id):
		self.__collection.remove({'_id': mongo_id})
		
	def find_new_tasks(self, from_s, password):
		for job in self.__jobs.find({"new-task": "y"}):
			receivers = Receivers([self.get_email(job['to'])], [job['to']])
			sender = Sender(from_s, job['from'])
			
			body = """This is an automated message. 
You are receiving this, because you have been assigned a new job.

Subject: {subject}
Job Duration: {date_c} - {date_d}

{message}
""".format(subject=job["subject"], date_c=job["date-created"], date_d=job["date-due"], message=job["message"])	
			my_email = Email("smtp.gmail.com", 587, from_s, password)
			my_email.set_message(sender.from_string(), 
								receivers.to_string(0), 
								job["subject"],
								body
								)
			my_email.send(sender.get_sender(), receivers.get_receiver(0))
	
	def get_email(self, username):
		return self.__employees.find_one({"username": username})["email"]

