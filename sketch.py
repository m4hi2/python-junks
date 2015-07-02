'''-----------------------------------------------------------------------------
This file has evolved a lot, and now this is going to be my I/O play gorund;
-----------------------------------------------------------------------------'''
man = []
other = []

try:
  data = open("sketch.txt")
  for line in data:
    try:
      (role, line_spoken) = line.split(':', 1)
      line_spoken = line_spoken.strip()
      if role == "Man":
        man.append(line_spoken)
      elif role == "Other Man":
        other.append(line_spoken)
    except ValueError:
      pass
  print(man)
  print(other)
  try:
    man_data = open("man_data.txt", "w")
    other_data = open("other_man_data.txt", "w")
    print(man, file= man_data)
    print(other, file = other_data)
    man_data.close()
    other_data.close()
    print("\n", "Job done")
    
  except IOError:
    print("You fucker, where is my file in the system?")

  finally:
    man_data.close()
    other_data.close()
    
    
except IOError:
  print("Fuck, You forgot to put the file in")
  

finally:
  data.close()
    
      
      
      
      
