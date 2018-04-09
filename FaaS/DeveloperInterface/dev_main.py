import pickle
import sys
import os

curr_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'creds.pckl'))

def process_developer_input():
	
	logged_in = True
	current_user = ""
	## Loading the user credentials map
	try:
		with open(curr_path, 'rb') as f:
			users = pickle.load(f)
			f.close()
		
	except IOError:
		users = {}
	
	while True:
		cmd = raw_input('Enter your command:')

		cmdps = cmd.split(" ")
		
		if cmdps[0] == "quit":
			print ("Goodbye!")
			break
			
		elif cmdps[0] == "login" and len(cmdps) == 3:
			username = cmdps[1]
			password = cmdps[2]
			
		elif cmdps[0] == "signup" and len(cmdps) == 3:
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
			
		else:
			print("Invalid Command, enter again")
			
	f = open(curr_path, 'wb')
	pickle.dump(users, f)
	f.close()

	return "Test"