# input: ali ahmed, yasser alwan, mouhamed hasan
names = input (" write the names sapareted by comama :").split(", ")
#output ["ali ahmes", "yasser alwan", "mouhamed hasan"]
for x in names:
  single_names=  x.split(" ")
#['ali', 'ahmed']
# ['yasser', 'alwan']
# ['mouhamed', 'hasan']
  result = []
  for a in single_names:
     print (a)
     capitalize_names = a.capitalize()
     result.append(capitalize_names)
  print (result)
  