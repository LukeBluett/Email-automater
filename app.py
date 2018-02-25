#!/usr/bin/python3

import smtplib

sender = ''
receivers = ['']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain>
Subject: SMTP e-mail test

This is a test e-mail message
"""

try:
	smtp_object = smtplib.SMTP(smtp_address, smtp_port)
	smtp_object.sendmail(sender, receivers, message)
	print("Success: Email was sent")
except SMTPException:
	print("Failed: Email was not delivered")
	
