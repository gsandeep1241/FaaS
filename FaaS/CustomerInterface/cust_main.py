import sys
import os
import datetime
import time
import cPickle as pickle

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../')))
import event_object_generator as eog

def process_customer_input():
	while True:
		cmd = raw_input('Enter your command:')

		if cmd == "quit":
			print ("Goodbye!")
			break
			
		cmdps = cmd.split(" ")
		if len(cmdps) < 2:
			print("Error: Invalid Command")
			continue
		event_object = eog.generate_object(cmd)
		
		if event_object["url"] == "":
			print("Error: Invalid URL.")
			continue
			
		if (len(cmdps) == 2 and cmdps[0] == "get") or (len(cmdps) == 3 and cmdps[0] == "put") \
		or (len(cmdps) == 3 and cmdps[0] == "post") or (len(cmdps) == 2 and cmdps[0] == "delete"):
			
			file_name = str(time.time()).strip() + '.pckl'
			file = os.path.abspath(os.path.join(os.path.dirname(__file__),'WriteContent/' + file_name))
			
			f = open(file, 'wb')
			pickle.dump(event_object, f)
			f.close()
			
			#write listener and print output
			while True:
				listener_file = os.path.abspath(os.path.join(os.path.dirname(__file__),'ReadContent/' + file_name))
				try:
					with open(listener_file, 'rb') as f:
						event_obj = pickle.load(f)
						f.close()
						print(event_obj)
						os.remove(listener_file)
						break
						
				except IOError:
					time.sleep(1)
					continue
			
		else:
			print("Error: Invalid Command")

	return "Test"