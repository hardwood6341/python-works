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

#subproject 5
# print("***welcome to the multiplication table***")
# x= int (input ("enter a  number:"))
# for y in range(1,11):
#     c = x * y
#     print (x ,"*" , y ,"=", c)

#subproject 6
# print ("**** Welcom to iShop calculator ****")
# basket = []
# cost = []
# c = int (input ("\nHow many items are there in your basket today?: "))
# if c == 0:
#     print ("you come not to buy thinks, so just goaway")
# else:
#  print ("\nLet's get to counting them...")
#  for y in range (1,c+1):
#   a = input (f"Please tell me the name of the item number {y}: ") 
#   basket.append(a)
#   n =  input (f"What is the price of {a}: ").split('$') #output ['1.1','']
#   for y in n:
#         if y:
#          cost.append(float(y))
#  b = input ("Would you like to see your entire basket items? (yes or no): ").lower()
#  if b != 'yes':
#     input ("press enter to exit")
    
#  else:
#     print (basket)
#     d = input ("Would you like to see how much it'll cost?( yes or no): ").lower()
#     if d != 'yes':
#         input ("press enter to exit")
#     else:
#         print (sum(cost))