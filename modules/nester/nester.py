"""
This is the most idiotic module ever written -_- fuckers made me do it;
bal chal;

"""
import sys
def print_lol (the_list,indent= False,  tab_width=0,of=sys.stdout, e = "" ):
  for each_item in the_list:
    if isinstance (each_item, list):
      print_lol (each_item,indent, tab_width+1, of, e)
    else:
      if indent:
          for each in range(tab_width):
            print ("\t ", end=e ,file = of)
      print (each_item, end = e, file= of)
