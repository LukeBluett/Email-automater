import smtplib
from smtplib import *

class Email:
	def __init__(self, smtp_address, smtp_port, username, password):
		self.__smtp_object = smtplib.SMTP(smtp_address, smtp_port)
		self.__smtp_object.ehlo()
		self.__smtp_object.starttls()
		self.__smtp_object.login(username, password)

	def set_message(self, from_s, to_s, subject, body):
		self.__message = """{f} 
{t} 
Subject: New Task : {s}
							
{b}
""".format(f=from_s, t=to_s, s=subject, b=body)

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
		return 	"""To: {name} 
				< {receiver} >\n""".format(name=self.__names[index], receiver=self.__receivers[index])

class Sender:
	def __init__(self, sender, name):
		self.__sender = sender
		self.__name = name
		
	def get_sender(self):
		return self.__sender

	def from_string(self):
		return 	"""From: {name} 
				< {sender} >\n""".format(name=self.__name, sender=self.__sender)


