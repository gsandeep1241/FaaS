import pickle

def process_developer_input():

	## Loading the user credentials map
	try:
		with open('../FaaS/DeveloperInterface/creds.pckl', 'rb') as f:
			users = pickle.load(f)
			f.close()
		
	except IOError:
		users = {}
	
	for k in users:
		print(k + users[k])
	
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
			
		else:
			print("Invalid Command")
			
	f = open('../FaaS/DeveloperInterface/creds.pckl', 'wb')
	pickle.dump(users, f)
	f.close()

	return "Test"