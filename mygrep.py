import sys
import os

def print_match(flags,line,i,file_name):
	result=""
	if('-n' in flags):
		result+=f"{i+1}"

	if(not '-h' in flags):
		result+=f" {file_name}"
	result+=f" {line}"
	print(result)

def grep(pattern,file_name,flags,from_dir):
	try:
		with open(file_name,'r') as file:
			lines = file.readlines()
			for i,line in enumerate(lines):
				_line = line

				if('-i' in flags):
					pattern = pattern.lower()
					_line = line.lower()


				if(pattern in _line):
					print_match(flags,line,i,file_name)


	except Exception as e:
		if(not from_dir):
			print(f"Unable to read file.Please provide valid file: {e} {file_name}")
		# exit(0)

def parse_args():
	flags ,non_flags = [], []

	for i in sys.argv:
		if(i[0] == '-'):
			flags.append(i)
		else:
			non_flags.append(i)

	if(len(non_flags)<3):
		print("Not Enough Arguments")
		exit(0)

	pattern = non_flags[1]
	file_name = non_flags[2]
	isExist = os.path.exists(file_name) 

	if(not isExist):
		print("Please provide valid file path")
		exit(0) 
	return (pattern,file_name,flags)

def process_file_path(pattern,file_name,flags):
	if os.path.isfile(file_name):
		grep(pattern,file_name,flags,from_dir=False)
	else:
		files = os.listdir(file_name)
		for f in files:
			f=os.path.join(file_name,f)
			if os.path.isfile(f):
				grep(pattern,f,flags,from_dir=True)
			else:
				process_file_path(pattern,f,flags)

if __name__ == '__main__':
	pattern,file_name,flags = parse_args()
	process_file_path(pattern,file_name,flags)
