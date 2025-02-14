#difficult projects

#!project 1 (حلقه رقم 50)
#! method 1
# TODO: write the names separated by comma :
# input: ali ahmed, yassir alwan, mohamed hasan
# output :   ['Ali', 'Ahmed']
#             ['Yasser', 'Alwan']
#             ['Mouhamed', 'Hasan']
#             abbrevated_Names:
#             A.A.
#             Y.A.
#             M.H.
#* method 1
#NOTE: input: ali ahmed, yasser alwan, mouhamed hasan
names = input (" write the names separated by comma :").split(", ")
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
print ("abbreviated_Names:")
for x in names:
  single_names=  x.split(" ") 
  for b in single_names:
    capitalize_names = b.capitalize()
    capitalize_letter.append(capitalize_names[0])
for i in range(0, len(capitalize_letter),2):
    print(f"{capitalize_letter[i]}.{capitalize_letter[i+1]}.")

#! method 2 (اذا المستخدم ادخل حروف كبيره)
names = input ( 
  "Enter the first and last name of your friends separate by comma:").split(", ")
print ("\n".join(names))
print("abbrevated names:")
for name in names:
  separate_name=name.split()
  first_word = separate_name[0]
  second_word = separate_name[1]
  first_letter=first_word[0]
  second_letter=second_word[0]
  print (f"{first_letter}.{second_letter}.")

#!project 2 (حلقه رقم 50)
#TODO: Enter a sentence
    #* input: how are you
#output: you are how

#NOTE: input: how are you
s = input ("Enter a sentence : ").split(" ")
#? output: ["how","are","you"]
print (" ".join(s[-1: :-1]))
#? output  
#? you are how
#? output (print (s[-1: :-1]))
#?  ['you', 'are', 'how']
