import sys
import os
import pickle

rev_keys_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'DeveloperInterface/rev_keys.pckl'))

def generate_object(cmd):
	cmd_parts = cmd.split(" ")
	
	try:
		with open(rev_keys_path, 'rb') as f:
			rev_keys = pickle.load(f)
			f.close()
		
	except IOError:
		rev_keys = {}
		
	dict = {}
	dict['type'] = cmd_parts[0];
	
	url_parts = cmd_parts[1].split("/")
	
	dict['url'] = url_parts[0];
	
	if url_parts[0] not in rev_keys:
		return {"url": ""}
	
	dict['key'] = rev_keys[url_parts[0]][1]
	dict['content_uri'] = ""
	
	for i in range(1, len(url_parts)):
		dict['content_uri'] += url_parts[i] + "/"
	
	if len(cmd_parts) > 2:
		dict['data'] = cmd_parts[2];
		
	return dict