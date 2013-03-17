import os
import time
import sys

os.system('clear')
deviceIP = raw_input("Enter the IP address to listen for: ")
cacheFolder = "cache/"
cacheFileName = time.time()
filePath = cacheFolder + str(cacheFileName)

def checkForDevice():
	# See if the device has connected to the network
	systemCommand = "sudo arp-scan -l > " + filePath
	os.system(systemCommand)
	with open(filePath) as fileObj:
		for line in fileObj.readlines():
			if deviceIP in line:
				success = True
				break
			else:
				success = False
	return success

def delayPrint(text):
	print text
	time.sleep(2)

def promptToRestart():
	os.system('clear')
	userChoice = raw_input("restart or exit? ")
	if (userChoice == 'restart'):
		connectionDaemon()
	elif(userChoice == 'exit'):
		exit()
	else:
		delayPrint('Invalid selection!')
		promptToRestart()

def connectionActions():
	# Do this stuff when connected
	import smtplib
	try:
		server = smtplib.SMTP( "smtp.gmail.com", 587 )
		server.starttls()
		server.login( '<email address>', '<email pass>' )
		server.sendmail( '<from>', '<to>', '<message>' )
	except:
		delayPrint('Connection failed')
		connectionDaemon()
	delayPrint('SMS sent!')
	promptToRestart()
	pass

def connectionDaemon():
	i = 0
	while (i == 0):
		# Keep on searching, yo! (Indefinitely)
		connected = checkForDevice()
		if (connected == True):
			os.system('clear')
			print "Device is ONLINE"
			connectionActions()
		else:
			os.system('clear')
			print "Device is OFFLINE"

connectionDaemon()
