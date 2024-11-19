import sys
import os

def print_match(flags,line,i):
	if('-n' in flags):
		print(f"{i+1}:{line}")
	else:
		print(f"{line}")


def grep(pattern,file_name,flags):
	try:
		with open(file_name,'r') as file:
			lines = file.readlines()
			for i,line in enumerate(lines):
				_line = line

				if('-i' in flags):
					pattern = pattern.lower()
					_line = line.lower()


				if(pattern in _line):
					print_match(flags,line,i)


	except Exception as e:
		print("Unable to read file.Please provide valid file")
		exit(0)

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

if __name__ == '__main__':
	pattern,file_name,flags = parse_args()
	grep(pattern,file_name,flags)
