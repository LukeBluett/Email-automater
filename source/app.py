import smtplib
from smtplib import *
import argparse
import dbhandler
import my_email
from dbhandler import *
from my_email import *
import getpass
import time


def check_status():
	return 0
	
def send_mails():
	return 0
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--email", help="Set email of sender")
	parser.add_argument("-n", "--name", help="Set name of sender")

	args = parser.parse_args()
	
	sender = ""
	name = ""
	password = ""
	if args.email:
		sender = args.email

	if args.name:
		name = args.name
		
	password = getpass.getpass("Password: ")
	count = 0
	dbHandler = DBHandler('172.17.0.2', 27017, "rcc")
	while(True):
		dbHandler.find_new_tasks(sender, password)
		time.sleep(30)
		print("Hi " + str(count))
		count += 1
	"""
	sender2 = Sender(sender, name)
	receivers = Receivers([sender], [name])
	my_email2 = Email("smtp.gmail.com", 587, sender2.get_sender(), password)
	my_email2.set_message(sender2.from_string(), receivers.to_string(0), "Test subject", "test body")
	my_email2.send(sender2.get_sender(), receivers.get_receiver(0))
	"""
	
