# input: ali ahmed, yasser alwan, mouhamed hasan
names = input (" write the names sapareted by comama :").split(", ")
#output ["ali ahmes", "yasser alwan", "mouhamed hasan"]
for x in names:
  single_names=  x.split(" ")
#['ali', 'ahmed']
# ['yasser', 'alwan']
# ['mouhamed', 'hasan']
  for a in single_names:
     capitalize_names = a.capitalize
     print (capitalize_names) 
  # output ahmed alsaedS