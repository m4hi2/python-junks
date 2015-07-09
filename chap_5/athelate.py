'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
james = [ ]
julie = [ ]
mikey = [ ]
sarah = [ ]
def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs 

try:
	with open("james.txt") as james_data, open("julie.txt") as julie_data, open("mikey.txt") as mikey_data,open("sarah.txt") as sarah_data: #oepns all the files
		james.extend(james_data.readline().strip().split(",")) #1 read a line from the file
		julie.extend(julie_data.readline().strip().split(",")) #2 strips off new line and white spaces
		mikey.extend(mikey_data.readline().strip().split(",")) #3 
		sarah.extend(sarah_data.readline().strip().split(","))
#Now I'll print the fastest time for each of the runners 
	sanitized_james = []
	sanitized_julie = []
	sanitized_mikey = []
	sanitized_sarah = []
	for time in james:
		sanitized_james.append(sanitize(time))
	for time in julie:
		sanitized_julie.append(sanitize(time))
	for time in mikey:
		sanitized_mikey.append(sanitize(time))
	for time in sarah:
		sanitized_sarah.append(sanitize(time))

	print(sorted(sanitized_james))
	print(sorted(sanitized_julie))
	print(sorted(sanitized_mikey))
	print(sorted(sanitized_sarah))
#This will handle any error during the file I/O
except IOError as IOerr:
	print("File Err:" + str(IOerr))
except ValueError as verr:
	print("Valu Err:" + str(verr))