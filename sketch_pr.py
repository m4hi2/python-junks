from print_endl import print_endl
import os


try:
  drama = open("sketch.txt")

  for line in drama:
    try:
      line.find(":") == -1
      (role,  speech) = line.split(":", 1)
      print_endl(role)
      print_endl("said:")
      print_endl(speech)
      
      
    except ValueError:
      pass
  drama.close()
except IOError:
  print_endl("Fuck, you forgot to put the thing(data file) in")

#this is my playground for IO.
