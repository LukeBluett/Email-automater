import argparse, configparser, getpass, smtplib, time
import dbhandler, my_email
from smtplib import *
from dbhandler import *
from my_email import *
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-d', '--database', help='Set Database for mongodb')
	parser.add_argument('-e', '--email', help='Set email of sender')
	parser.add_argument('-c', '--config', help='Pass in config file')
	parser.add_argument('-i', '--ip', help='Set ip address for mongodb')
	parser.add_argument('-n', '--name', help='Set name of sender')
	parser.add_argument('-p', '--port', help='Set port number for mongodb')

	args = parser.parse_args()
	
	sender = ''
	name = ''
	password = ''
	ip_address = ''
	port_no = 0
	database = ''
	
	if args.email and args.name and args.ip and args.port and args.database:
		sender = args.email
		name = args.name
		password = getpass.getpass('Password')
		ip_address = args.ip
		port_no = args.port
		database = args.database

	if args.config:
		config = configparser.ConfigParser()
		config.read(args.config)
		sender = config.get('email', 'address')
		name = config.get('email', 'name')
		ip_address = config.get('mongo', 'address')
		port_no = int(config.get('mongo', 'port'))
		password = getpass.getpass('Password:')
		database = config.get('mongo', 'database')
		
	dbHandler = DBHandler(ip_address, port_no, database)
	while(True):
		dbHandler.find_new_tasks(sender, password)
		time.sleep(3600)
		
	
