# Daily calendar
import smtplib  # pkg for sending mail. 
my_address = "jm273606@gmail.com"
headers = ['Subject: Daily Calendar',
	'From: ' + my_address,
	'To: ' + my_address,
	]
Entries = open('my_calendar').readlines() [:10]
msg = '\r\n'.join(headers)+ '\r\n' + '' .join(entries)

smtp = smtplib.SMTP('mail') #replaces mail with "gmail"
smtp.sendmail (my_address, [my_address], msg,)
smtp.close()