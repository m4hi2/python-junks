'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
james = []
julie = []
mikey = []
sarah = []
try:
	with open("james.txt", 'r') as james_data, open("julie.txt", 'r') as julie_data, open("mikey.txt", 'r') as mikey_data,open("sarah.txt", 'r') as sarah_data: #oepns all the files
		james.extend(james_data.readline().strip().split(",")) #1 read a line from the file
		julie.extend(julie_data.readline().strip().split(",")) #2 strips off new line and white spaces
		mikey.extend(mikey_data.readline().strip().split(",")) #3 
		sarah.extend(sarah_data.readline().strip().split(","))
#Now I'll print the fastest time for each of the runners 
	print(sorted(james))
	print(sorted(julie))
	print(sorted(mikey))
	print(sorted(sarah))
#This will handle any error during the file I/O
except IOError as IOerr:
	print("File Err:" + str(rr))
