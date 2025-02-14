#prject 16 useing split & choice (wallet project)

#method 1
import random
print ("Welcme to 'whose wallet?'")
print ("You will give me a list of names, and I will pick a person to pay")
a = input ("If you're ready, enter the names separated by a comma: ").split(", ")
b = int (len(a) -1)
c = random.randint(0,b)
d = a[c]
print (f"Please ask '{d}' to take his wallet out. Dinner is on him")

#method 2 
import random
print ("Welcme to 'whose wallet?'")
print ("You will give me a list of names, and I will pick a person to pay")
a = input ("If you're ready, enter the names separated by a comma: ").split(", ")
d = random.choice(a)
print (f"Please ask '{d}' to take his wallet out. Dinner is on him")

#using insert
# a = [1,2,4]
# a.insert(2,3)
# print (a)

#لازم تعرف استخدام spilt و choice 