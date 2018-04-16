import sys
import os
import datetime
import time
import pickle

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
			
		if (len(cmdps) == 2 and cmdps[0] == "get") or (len(cmdps) == 3 and cmdps[0] == "put") \
		or (len(cmdps) == 3 and cmdps[0] == "post") or (len(cmdps) == 2 and cmdps[0] == "delete"):
			
			file_name = str(time.time()).strip() + '.pckl'
			file = os.path.abspath(os.path.join(os.path.dirname(__file__),'WriteContent/' + file_name))
			
			f = open(file, 'wb')
			pickle.dump(event_object, f)
			f.close()
			
		#write listener and print output
			
		else:
			print("Invalid Command, enter again")

	return "Test"