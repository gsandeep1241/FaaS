import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../')))
import event_object_generator as eog

def process_customer_input():
	while True:
		cmd = raw_input('Enter your command:')

		if cmd == "quit":
			print ("Goodbye!")
			break
			
		cmdps = cmd.split(" ")
		
		if len(cmdps) == 2 and cmdps[0] == "get":
			# generate event object
			event_object = eog.generate_object(cmd)
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