import cPickle as pickle
import sys
import os
import string
import random
import json
from pprint import pprint
from shutil import copyfile

creds_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'creds.pckl'))
keys_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'keys.pckl'))
rev_keys_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'rev_keys.pckl'))
dev_content_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../../Developer/DeveloperContent/'))
dev_store_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../Storage/'))

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
		
	## Loading reverse-keys from rev-keys map
	## Format: {"url" : ["usr", "key"]}
	try:
		with open(rev_keys_path, 'rb') as f:
			rev_keys = pickle.load(f)
			f.close()
		
	except IOError:
		rev_keys = {}
	
	
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
			rev_keys[URL] = [current_user, ID]
			
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
				
		elif len(cmdps) == 4 and cmdps[0] == "deploy":
			
			if logged_in == False:
				print("You are not logged in, Please login and try")
				continue
			
			ID = cmdps[1]
			if ID not in keys:
				print("Key does not exist")
				continue
			
			try:
				with open(os.path.join(dev_content_path,cmdps[3])) as data_file:
					data = json.load(data_file)
			
			except StandardError:
				print("Configuration file error")
				continue
				
			new_dir_path = os.path.join(dev_store_path, ID) 
			
			if not os.path.exists(new_dir_path):
				os.makedirs(new_dir_path)
				
			copyfile(os.path.join(dev_content_path, cmdps[2]), os.path.join(new_dir_path, "main.py"))
			
			dict = {}
			for handler in data["handlers"]:
				dict[handler["type"]] = handler["handler"]
			
			pckl_path = os.path.join(new_dir_path, 'config.pckl')
			f = open(pckl_path, 'wb')
			pickle.dump(dict, f)
			f.close()
					
		else:
			print("Invalid Command, enter again")
			
	f = open(creds_path, 'wb')
	pickle.dump(users, f)
	f.close()
	
	f = open(keys_path, 'wb')
	pickle.dump(keys, f)
	f.close()
	
	f = open(rev_keys_path, 'wb')
	pickle.dump(rev_keys, f)
	f.close()
	
	

	return "Test"