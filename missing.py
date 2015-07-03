try:
  data = open('missing.txt')
  print(data.readline(), end= '')
except:
  print('Fuck, You forgot to put the file in')
finally:
  if 'data' in locals():
    data.close()
