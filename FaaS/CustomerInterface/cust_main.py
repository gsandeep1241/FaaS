def process_customer_input():
	while True:
		cmd = raw_input('Enter your command:')

		if cmd == "quit":
			print ("Goodbye!")
			break
			
		cmdps = cmds.split(" ")
		
		if len(cmdps) == 2 and cmdps[0] == "get":
			## initiate get request
			L = 0
			
		elif len(cmdps) == 3 and cmdps[0] == "put":
			## Initiate put request
			L = 0
		
		elif len(cmdps) == 3 and cmdps[0] == "post":
			## Initiate post request
			L = 0
			
		elif len(cmdps) == 2 and cmdps[0] == "delete":
			## Initiate delete request
			L = 0
			
		else:
			print("Invalid Command, enter again")

	return "Test"