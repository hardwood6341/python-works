#project 20 loop (for)
#subproject 1
ASCII = {2:"""
██████╗░
╚════██╗
░░███╔═╝
██╔══╝░░
███████╗
╚══════╝""", 4:"""
░░██╗██╗
░██╔╝██║
██╔╝░██║
███████║
╚════██║
░░░░░╚═╝""", 6: """
░█████╗░
██╔═══╝░
██████╗░
██╔══██╗
╚█████╔╝
░╚════╝░""", 8:"""
░█████╗░
██╔══██╗
╚█████╔╝
██╔══██╗
╚█████╔╝
░╚════╝░ """, 9: """
░█████╗░
██╔══██╗
╚██████║
░╚═══██║
░█████╔╝
░╚════╝░""", 10: """ 
░░███╗░░░█████╗░
░████║░░██╔══██╗
██╔██║░░██║░░██║
╚═╝██║░░██║░░██║
███████╗╚█████╔╝
╚══════╝░╚════╝░"""}
numbers = [1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x % 2 == 0:
         print ("the number is",ASCII[x])
print ("the loop Even numbers is finshed seccsifly")
for x in numbers:
     if x > 8 : 
         print (ASCII[x])
print ("the loop greated than 8 numbers is finshed seccsifly")

#subproject 2
# attendees = ["ali", "mouhamed", "ibrahim"]
# for person in attendees:
#     print (person)
#     a = input ("is this person attending? (yes/no):").lower()
#     if a != 'yes':
#         print ("Attendance not confirmed")
        
#     else:
#      print ("attendance confirmed")
#     print ("-------")

#subproject 3
# a = input ("Enter the names of attendees separated by commas:").lower()
# b = a.split(", ")
# for y in b:
#    print ("\n",y,"\n")
#    c = input ("is this person attending? (Yes or no)").lower()
#    if c == 'yes':
#       print ("attendance conformed")
#    else:
#       print ("attendance not conformed")
#    print ("________")  

#    #subproject 4
# good = []
# not_good = []
# a = input("Enter your tasks for today separated by commas: ").split(", ")
# for y in a:
#     c = input(f"Did you finish {y} already?").lower()
#     if c == 'yes':
#         good.append(y)
#         print("Nice job!")
#     else:
#         not_good.append(y)
#         print("Try not to put it down")
# print(f"***** Done tasks ***** {good}")