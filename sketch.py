'''-----------------------------------------------------------------------------
This file has evolved a lot, and now this is going to be my I/O play gorund;
-----------------------------------------------------------------------------'''
import pickle

man = []
other_man = []
try:
  with open("sketch.txt") as data, open("man_data.txt", "wb") as man_data, open("other_man_data.txt", "wb") as other_data:
    for line in data:
      try:
        (role, line_spoken) = line.split(":", 1)
        if role == "Man":
          man.append(line_spoken)
          
        elif role == "Other Man":
          other_man.append(line_spoken)
          
      except:
        pass
    pickle.dump(man,man_data)
    pickle.dump(other_man,other_data)

except IOError as err:
  print('File error: ' + str(err)) 
