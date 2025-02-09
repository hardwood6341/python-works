a = input("Enter the first and last name of your friends separated by comma:").split(", ")
# output ['ali ahmed', 'yasser alwan', 'mouhamed hasan']
result = []
for name in a:
   a= name.split(" ")
   a= name.capitalize()
   result.extend(a)
# output ['ali', 'ahmed', 'yasser', 'alwan', 'mouhamed', 'hasan']
print (result)