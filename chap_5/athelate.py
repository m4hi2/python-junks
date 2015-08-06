'''
The coach needs the fastest racer but he's an asshole. He saved data like an idiot with various formats.
So, I need to stick my ass to the chair for a bit longer and format down his mess.
It's really messy, did any one say messi? :D
'''
#Takes string input then converts it to a '.' seperator if the seperator is either ":" or '-'
def sanitize(time_string): 
	'''The raw data "times" have either "-" or ":" or "." seperator which is not a good thing for the sort or 
	sorted Function. So this helps to convert all into "." seperator '''
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return time_string
	(mins, secs) = time_string.split(splitter)
	return mins + "." + secs #The time is retuned with "." seperator string value
#Defining class "Athlete" for all the Athletes :D
#This class "MUST" be initialized in get_data() function, otherwise things won't work actually
class AthleteList(list):
	"""docstring for AthleteList"""
	def __init__(self, name, dob = None, time = []):
		list.__init__([])
		self.name = name
		self.dob = dob
		self.extend(time)
	def top3(self):
		return sorted(sanitize(t) for t in self)[0:3]		
#Function to raed file's line from the drive and split it on comma 
#This function also returns an object to work on
def get_data(filename):
	try:
		with open(filename) as file: #Opens up the file assigned to a variable, named "file"
			file_data = file.readline().strip().split(",") #Reads a line (a single line in this case) and stips and splits on ","
			return AthleteList(file_data.pop(0), file_data.pop(0), set(file_data))
			#returns a object with name, date_of_birth and times
	except IOError as IOerr:
		#handles any I/O Error if the file is missing or something else
		print("Where's ma file bae?" +  str(IOerr)) #Funny message to make no sense with
		return None
#Creating objects based on the Athlete class
sarah = get_data("sarah2.txt")
#Printing the Data  out
print(sarah.name + "'s top 3 times are" + str(sarah.top3()))
