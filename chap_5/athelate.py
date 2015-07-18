'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
#Takes string input then converts it to a '.' seperator if the seperator is either ":" or '-'
def sanitize(time_string): 
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs 
#Defining class "Athlete" for all the Athletes :D
class Athlete():
	"""docstring for Athlete"""
	def __init__(self, name, dob=None, time= []):
		super(Athlete, self).__init__()
		self.name = name
		self.dob = dob
		self.time = time
	def top3(self, time):
		return sorted(sanitize(t) for t in time)[0:3]

#Function to raed file's line from the drive and split it on comma starts 
def get_data(filename):
	try:
		with open(filename) as file:
			file_data = file.readline().strip().split(",")
			return Athlete (file_data.pop(0), file_data.pop(0), file_data)


	except IOError as IOerr:
		print("Where's ma file bae?" +  str(IOerr))
		return None
sarah = get_data("sarah2.txt")
print(sarah.name + "'s top 3 times are" + str(sarah.top3(sarah.time)))