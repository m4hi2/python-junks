'''-----------------------------------------------------------------------------
This file has evolved a lot, and now this is going to be my I/O play gorund;
-----------------------------------------------------------------------------'''
man = []
other = []

try:
  data = open("sketch.txt")
  for line in data:
    try:
      (role, line_spoken) = data.split(':', 1)
      line_spoken = line_spoken.stip()
      if role == "Man":
        man.append(line_spoken)
      elif role == "Other Man":
        other.append(line_spoken)
    except ValueError:
      pass
    data.close()
except IOError:
  print("Fuck, You forgot to put the file in")
    
    
      
      
      
      
