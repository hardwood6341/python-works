#project 12 Guess the computer PIN code

#first method
import random 
pc_value = random.randint(1000,9999)

a = int (input ("Enter a 4-digit PIN code:"))
if a < 1000 :
  print ("Plese Enter 4 digits")
elif a >= 1000 and a <= 9999:
 if a == pc_value :
   print (" correct answer")
 else :
   print ("Failure! PIN code did not match.")
   print (f"the computer generated this PIN: {pc_value}")
else:
 print ("please enter 4 digits")

#second method 
# import random 
# pc_value = random.randint(1000,9999)
# a = int (input ("Enter a 4-digit PIN code:"))

# if len (str (a)) != 4: 
#   print ("Plese Enter 4 digits")
# elif a == pc_value :
#    print (" correct answer")
# else :
#    print ("Failure! PIN code did not match.")
#    print (f"the computer generated this PIN: {pc_value}")

# (!=) هذا الرمز يعني لا يساوي    ❤️
# len تستخدم في معرفه عدد احرف النص    ❤️

