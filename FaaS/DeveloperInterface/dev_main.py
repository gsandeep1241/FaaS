def process_developer_input():

	## Loading the user credentials map
	

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
		
	return "Test"