#first pipeline

import json
from importlib.abc import Loader

import yaml
import sys

def is_yaml(filename):
	return 'yaml' in filename

def do_yaml_to_json(filename):
	pass
	print("do yaml to json")
	f = open(filename, 'r') #opening the file to be read
	data = yaml.load(f.read(), Loader=yaml.FullLoader) #yaml.load takes in a string(file of strings in this case) and converts it to a yaml object
	tdata = json.load(data) #taking the yaml object and turning it into a json object
	output_filename = filename.replace('.yaml', '.json') #taking the file name and replacing to the correct extension for conversion

	outputfile = open(output_filename, 'w') #taking the converted extension file and writing into it
	outputfile.write(tdata) #taking the converted object and writing it into the converted extension file
	f.close()
	outputfile.close()

def do_json_to_yaml(filename):
	pass
	print("do json to yaml")
	f = open(filename, 'r')

# step 2
	data = json.loads(f.read())

# step 3
	##print(type(data), data)
	tdata = yaml.dump(data)
	output_filename = filename.replace('.json', 'yaml')
	##print('putout: ', output_filename)

	outputfile = open(output_filename, 'w')
	outputfile.write(tdata)

# cleanup
	f.close()
	outputfile.close()	

if __name__== '__main__':
	#filename = "donuts.json"
	if len(sys.argv) != 2:
		print("you forgot the filename")
		exit()
	print('args: ', sys.argv)
	filename = sys.argv[1]
	if is_yaml(filename):
		do_yaml_to_json(filename)
	else:
		do_json_to_yaml(filename)

