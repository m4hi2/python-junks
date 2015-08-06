import pickle #This perticular program needs to pickle data
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
		return Non
#Following function makes the way for saving the data into file with pickle
def put_to_store(file_list):
	all_athletes = {}
	for each_file in file_list:
		athlete = get_data(each_file)
		all_athletes[athlete.name] = athlete
	try:
		with open("athletes.pickle", "wb") as file:
			pickle.dump(all_athletes, file)
	except IOError as IOerr:
		print("File Error in put_to_store():" +str(IOerr))
	return all_athletes
#Following function can easily fetch pickled data from the pickle file
def get_from_store(file):
	all_athletes = {}
	try:
		with open("athletes.pickle", 'wb') as file:
			all_athletes = pickle.load(file)
	except IOError as IOerr:
		print ("File Error in get_from_store():" + str(IOerr))
	return all_athletes