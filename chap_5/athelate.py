'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
james = [ ]
julie = [ ] 
mikey = [ ]
sarah = [ ]
def sanitize(time_string): #takes tring input then converts it to a '.' seperator if the seperator is either ":" or '-'
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs 

def get_data(filename):
	try:
		with open(filename) as file:
			return file.readline().strip().split(",")
	except IOError as IOerr:
		print("Where's ma file bae?" +  str(IOerr))
		return None

james = get_data("james.txt")
julie = get_data("julie.txt")
mikey = get_data("mikey.txt")
sarah = get_data("sarah.txt")

print("james:",sorted(set([sanitize(t) for t in james]))[0:3])
print("julie:",sorted(set(sanitize(t) for t in julie))[0:3])
print("mikey:",sorted(set(sanitize(t) for t in mikey))[0:3])
print("sarah:",sorted(set([sanitize(t) for t in sarah]))[0:3])
