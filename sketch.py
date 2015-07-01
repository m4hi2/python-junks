from print_endl import print_endl

drama = open ("sketch.txt")
for line in drama:
        if not line.find (":") == -1:
                (role, speech) = line.split (":", 1)
                print_endl (role)
                print_endl ("said:")
                print_endl (speech)
        else:
                print_endl(line)
               
