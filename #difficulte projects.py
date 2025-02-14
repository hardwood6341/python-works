#difficulte projects

#project 1
#TODO: write the names sapareted by comama :
# input: ali ahmed, yasser alwan, mouhamed hasan
# output :   ['Ali', 'Ahmed']
#             ['Yasser', 'Alwan']
#             ['Mouhamed', 'Hasan']
#             abbrevated_Names:
#             A.A.
#             Y.A.
#             M.H.

#NOTE: input: ali ahmed, yasser alwan, mouhamed hasan
names = input (" write the names sapareted by comama :").split(", ")
#output ["ali ahmes", "yasser alwan", "mouhamed hasan"]
for x in names:
  single_names=  x.split(" ")
#['ali', 'ahmed']
# ['yasser', 'alwan']
# ['mouhamed', 'hasan']
  result = []
  capitalize_letter = []
  for a in single_names:
    capitalize_names = a.capitalize()
    result.append(capitalize_names)
  print (result)
print ("abbrevated_Names:")
for x in names:
  single_names=  x.split(" ") 
  for b in single_names:
    capitalize_names = b.capitalize()
    capitalize_letter.append(capitalize_names[0])
for i in range(0, len(capitalize_letter),2):
    print(f"{capitalize_letter[i]}.{capitalize_letter[i+1]}.")