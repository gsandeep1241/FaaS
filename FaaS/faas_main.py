import cPickle as pickle
import sys
import os
from os import listdir
from os.path import isfile, join
import glob

read_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'CustomerInterface/WriteContent/'))
write_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'CustomerInterface/ReadContent/'))

def does_file_exist_in_dir(path):
	return any(isfile(join(path, i)) for i in listdir(path))

while True:
	if not does_file_exist_in_dir(read_path):
		continue
	
	file_name = ""
	for infile in sorted(os.listdir(read_path)):
		file_name = os.path.join(read_path, infile)
		event_obj = {}
		with open(file_name, 'rb') as f:
			event_obj = pickle.load(f)
			f.close()
			
		ID = event_obj['key']
		execute_base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'Storage'))
		execute_path = os.path.join(execute_base_path, ID)
		sys.path.insert(0, execute_path)
		
		import main
		
		ans = "temporary return string"
		try:
			with open(os.path.join(execute_path, 'config.pckl'), 'rb') as f:
				confs = pickle.load(f)
				f.close()
			
		except IOError:
			print("Error: Config file not found")
			continue
			
		type = event_obj["type"]
		handler = confs[type].rstrip()
		# handler = confs[type]

		content_uri = event_obj['content_uri']
		parts = content_uri.split('/')
		
		if parts[0] != confs["token"].rstrip():
			ans = "Error: Invalid URL."	
		
		elif  type == "get":
			if len(parts) != 2:
				ans = "Invalid URL"
			else:
				method_to_call = getattr(main, handler)
			
				ans = method_to_call(parts[1])
		
		elif type == "put":
			if len(parts) != 2:
				ans = "Invalid URL"
			else:
				content = event_obj['data']
				
				method_to_call = getattr(main, handler)
				ans = method_to_call(parts[1], content)
			
		elif type == "post":
			if len(parts) != 1:
				ans = "Invalid URL"
			else:
				content = event_obj['data']
				method_to_call = getattr(main, handler)
				ans = method_to_call(content)
				
		elif type == "delete":
			if len(parts) != 2:
				ans = "Invalid URL"
			else:
				method_to_call = getattr(main, handler)
			
				ans = method_to_call(parts[1])
			
		os.remove(file_name)
		file_name = os.path.join(write_path, infile)
		f = open(file_name, 'wb')
		pickle.dump(ans, f)
		f.close()
		print(infile + " file removed")
		break
		