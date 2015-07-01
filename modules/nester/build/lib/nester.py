"""
This is the most idiotic module ever written -_- fuckers made me do it;
bal chal;

"""
def print_lol (the_list,indent= False,  tab_width=0):
  for each_item in the_list:
    if isinstance (each_item, list):
      print_lol (each_item,indent, tab_width+1)
    else:
      if indent:
          for each in range(tab_width):
            print ("\t ", end="")
      print (each_item)
