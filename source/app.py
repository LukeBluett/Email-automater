#!/usr/bin/python3

import smtplib
import argparse

if __name__ == "__main__":
	parser = argparser.ArgumentParser()
	parser.add_argument("-e", "--email", help="Set email of sender")
	parser.add_argument("-n", "--name", help="Set name of sender")

	args = parser.parse_args()
	
	sender = ""
	name = ""
	if args.email:
		sender = args.email

	if args.name:
		name = args.name

	
