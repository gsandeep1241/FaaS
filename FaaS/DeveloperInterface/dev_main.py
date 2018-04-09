import pickle
import sys
import os
import string
import random

creds_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'creds.pckl'))
keys_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'keys.pckl'))

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

def url_generator(size=10, chars=string.ascii_lowercase + string.digits):
	return "www." + ''.join(random.choice(chars) for _ in range(size)) + ".com"
	
def process_developer_input():
	
	logged_in = False
	current_user = ""
	## Loading the user credentials map
	try:
		with open(creds_path, 'rb') as f:
			users = pickle.load(f)
			f.close()
		
	except IOError:
		users = {}
		
	## Loading keys from keys map
	## Format: {"key" : ["usr", "url"]}
	try:
		with open(keys_path, 'rb') as f:
			keys = pickle.load(f)
			f.close()
		
	except IOError:
		keys = {}
	
	while True:
		cmd = raw_input('Enter your command:')

		cmdps = cmd.split(" ")
		
		if cmdps[0] == "quit":
		
			print ("Goodbye!")
			break
			
		elif cmdps[0] == "login" and len(cmdps) == 3:
		
			if logged_in == True:
				print("Logout first and try")
				continue
			
			username = cmdps[1]
			password = cmdps[2]
			
			if not username in users or users[username] != password:
				print("Username or Password is incorrect")
				continue
			
			logged_in = True
			current_user = username
			
			print("User sucessfully logged in")
			
		elif cmdps[0] == "signup" and len(cmdps) == 3:
		
			if logged_in == True:
				print("Logout first and try")
				continue
		
			username = cmdps[1]
			password = cmdps[2]
			
			if username in users:
				print("Username already exists, enter again")
			
			elif len(password) < 5:
				print("Password is too short, enter again")
				
			else:
				users[username] = password
				logged_in = True
				current_user = username
				print("User created sucessfully")
				
		elif cmdps[0] == "logout" and len(cmdps) == 1:
			logged_in = False
			print("User logged out sucessfully")
			
		elif len(cmdps) == 2 and cmdps[0] == "generate" and cmdps[1] == "key":
			
			if logged_in == False:
				print("You can not generate keys, please login first")
				continue
				
			ID = id_generator()
			while ID in keys:
				ID = id_generator()
				
			URL = url_generator()
			keys[ID] = [current_user, URL]
			
			print("The generated key is : " + ID + " and the associated url is : " + URL)
				
		elif len(cmdps) == 3 and cmdps[0] == "show" and cmdps[1] == "url":
		
			if logged_in == False:
				print("You are not logged in, Please login and try")
				continue
				
			key_id = cmdps[2]
			
			if not key_id in keys:
				print("The entered key is wrong, check again")
			else:
				print("The URL associated with the provided key is : " + keys[key_id][1])
			
		else:
			print("Invalid Command, enter again")
			
	f = open(creds_path, 'wb')
	pickle.dump(users, f)
	f.close()
	
	f = open(keys_path, 'wb')
	pickle.dump(keys, f)
	f.close()

	return "Test"