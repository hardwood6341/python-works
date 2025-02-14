#project 18 the rabbit game (two wethods)

# print ("Welcome to place the rabbit")
# x = ['🌲', '🌲', '🌲']
# y = ['🌲', '🌲', '🌲']
# z = ['🌲', '🌲', '🌲']
# print ("Where should the rabbit go?")
# a =input ("Please choose a row and a column") 
# if a[0]  == '1' : 
#   c = int (a[1]) -1
#   x[c]= '🐇'
# if a[0]  == '2' : 
#   c = int (a[1]) -1
#   y[c]= '🐇'
# if a[0]  == '3' : 
#   c = int (a[1]) -1
#   z[c]= '🐇'
# print (x)
# print (y)
# print (z)

print ("Welcome to place the rabbit")
field = [['🌲', '🌲', '🌲'],['🌲', '🌲', '🌲'],['🌲', '🌲', '🌲']]
print (f"{field[0]} \n{field[1]} \n{field[2]}")
a =  input ("Please choose a row and a cloumn?")
x=  int (a[0]) -1
y= int (a[1]) -1
field[x][y] = '🐇'
print (f"{field[0]} \n{field[1]} \n{field[2]}")