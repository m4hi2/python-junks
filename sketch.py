'''-----------------------------------------------------------------------------
This file has evolved a lot, and now this is going to be my I/O play gorund;
-----------------------------------------------------------------------------'''
man = []
other_man = []

try:
  with open("sketch.txt") as data:
    for line in data:
      try:
        (role, line_spoken) = line.split(":", 1)
        if role == "Man":
          man.append(line_spoken)
        elif role == "Other Man":
          other_man.append(line_spoken)
      except:
        pass
  try:
    with open("man_data.txt", 'w') as man_data:
      print(man, file = man_data)
    with open("other_man_data.txt", 'w') as other_data:
      print(other_man, file = other_data)
  except IOError as irr:
    print("Where the fuck is the output file?" + str(irr))

except IOError as irr:
  print("Did you put in any input file?" + str(irr))
      
