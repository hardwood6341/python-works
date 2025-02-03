import random
print ("welcome to the coin Guessing Game!")
print ("""Chooose a method to toss the coin:
1. Using random.random() 
2. Using random.randint()""")
a = int (input ("enter your choise (1 or 2):"))
if a == 1:
  b = random.random() 
  if b> 0.5:
    c= "heads"
  else:
    c= "tails"
elif a== 2: 
  b= random.randint(0,2)
  if b >1:
    c= "heads"
  else:
    c= "tails"
else: 
  print ("invild entry")
d= input ("Enter your Guess (heads or tails):")
if d == c :
  print ("correct")
else:
  print (" you lose")