# attendees = ["ali", "mouhamed", "ibrahim"]
# for person in attendees:
#     print (person)
#     a = input ("is this person attending? (yes/no):").lower()
#     if a != 'yes':
#         print ("Attendance not confirmed")
        
#     else:
#      print ("attendance confirmed")
#     print ("-------")

a = input ("Enter the names of attendees separated by commas:").lower()
b = a.split(", ")
for y in b:
   print ("\n",y,"\n")
   c = input ("is this person attending? (Yes or no)").lower()
   if c == 'yes':
      print ("attendance conformed")
   else:
      print ("attendance not conformed")
   print ("________")  