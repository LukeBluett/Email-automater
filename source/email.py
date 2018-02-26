#!/usr/bin/python3

import smtplib

class Email:
	def __init__(self, smtp_address, smtp_port):
		self.__smtp_object = smtplib.SMTP(smtp_address, smtp_port)

	def set_message(self, from_string, to_string, subject, body):
		self.__message = 	from_string + "\n" +
							to_string + "\n" +
							subject + "\n\n" +
							body

	def send(self, sender, receiver):
		try:
			self.__smtp_object.sendmail(sender, receiver, self.__message)
		except SMTPException:
			print("Failed: Email was not delivered")

class Receivers:
	def __init__(self, receivers, names):
		self.__receivers = receivers
		self.__names = names

	def get_receiver(self, index):
		return self.__receivers[index]

	def to_string(self, index):
		return 	"To: To " + self.__names[index] + 
				" <" + self.__receivers[index] + ">"

class Sender:
	def __init__(self, sender, name):
		self.__sender = sender
		self.__name = name
		
	def get_sender(self):
		return self.__sender

	def from_string(self):
		return 	"From: From " + self.__name + 
				" <" + self.__sender + ">"


