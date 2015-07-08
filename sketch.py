'''-----------------------------------------------------------------------------
This file has evolved a lot, and now this is going to be my I/O play gorund;
-----------------------------------------------------------------------------'''
import nester

man = []
other_man = []
try:
  with open("sketch.txt") as data, open("man_data.txt", "w") as man_data, open("other_man_data.txt", "w") as other_data:
    for line in data:
      try:
        (role, line_spoken) = line.split(":", 1)
        if role == "Man":
          man.append(line_spoken)
          
        elif role == "Other Man":
          other_man.append(line_spoken)
          
      except:
        pass
    nester.print_lol(man, of= man_data,   e= "")
    nester.print_lol(other_man, of = other_data, e= "")

except IOError as err:
  print('File error: ' + str(err)) 
