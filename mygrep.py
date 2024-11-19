import sys
import os

def grep(pattern,file_name):
	try:
		with open(file_name,'r') as file:
			lines = file.readlines()
			for i,line in enumerate(lines):
				if(pattern.lower() in line.lower()):
					print(f"{i+1}:{line}")
	except Exception as e:
		print("Unable to read file.Please provide valid file")
		exit(0)

def parse_args():
	pattern = sys.argv[1]
	file_name = sys.argv[2]


	if(len(sys.argv)<3):
		print("Not Enough Arguments.Please provide pattern and file path")
		sys.exit(0)


	isExist = os.path.exists(file_name) 

	if(not isExist):
		print("Please provide valid file path")
		exit(0)
	return pattern,file_name

if __name__=='__main__':
	pattern,file_name = parse_args()
	grep(pattern,file_name)









# arguments = 
# f=open(file_name,'r')
# if('-n' in flags):
#     lines = f.readlines()
#     for i,line in enumerate(lines):
#         # print(line)
#         if(key in line):
#             print(f"{i+1}:{line}")