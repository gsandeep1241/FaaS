import sys
import os
import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../')))
import event_object_generator as eog

def process_customer_input():
	while True:
		cmd = raw_input('Enter your command:')

		if cmd == "quit":
			print ("Goodbye!")
			break
			
		cmdps = cmd.split(" ")
		event_object = eog.generate_object(cmd)
		
		if event_object["url"] == "":
			print("Invalid URL.")
			continue
		
		if len(cmdps) == 2 and cmdps[0] == "get":
			## initiate get request
			# generate time stamp and place event_object in a pckl file and put it in some destination with file name as event object
			#start a listener here to look for a file in a new location with  file name as the timestamp
			
			file_name = str(datetime.datetime.now()) + '.pckl'
			file = os.path.abspath(os.path.join(os.path.dirname(__file__),'WriteContent/' + filename))
			
			f = open(file, 'wb')
			pickle.dump(event_object, f)
			f.close()
			
			#write listener here
			
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