#project 21 how to use (import string)


#!حلقه 52 محلوله ب3 طرق
# TODO: Please type a sentence :
#* input : hello!#@
#* output : here is the same sentence without punctuation
#*          hello


#! method 1
import string
a = input (" Please type a sentence:")
#hello!
real_sentence =  []  #TODO خليته مجموعه
for i in a:
    
 if i not in string.punctuation:
       real_sentence.append(i)
                   #TODO لهذا السبب اشتغلت ابيند
print ("here is the same sentence without punctuation")
print ("".join(real_sentence))
 
#! method 2

import string
a = input (" Please type a sentence:")
#hello!
real_sentence =  []  #TODO خليته مجموعه
for i in a:
    
 if i not in string.punctuation:
       real_sentence.extend(i)
                   #TODO لهذا السبب اشتغلت اكستيند 
                   #TODO  الافضل اضافة الابيند لان المضاف هو عنصر واحد
print ("here is the same sentence without punctuation")
print ("".join(real_sentence))

#! method 3 

import string
a = input (" Please type a sentence:")
#hello!
real_sentence = "" #TODO  هنا هو متغير
for i in a:
    
 if i not in string.punctuation:
       real_sentence+=i
                   #TODO لهذا السبب اشتغلت ابيند
print ("here is the same sentence without punctuation")
print (real_sentence)

#! اختبار الحلقه 52
# TODO :
# Welcome to the password Generator!
# Enter the total number of characters in the password:
# Enter the total number of letters in the password:
# Enter the total number of numbers in the password: 
# Enter the total number of symbols in the password:

#* output : # Generated Password: U5~%bQ000u
#*             invild input! the total number is not equal with the entries


import string
import random 
print (" Welcome to the password Generator!")
total = int(input (" enter the total number of characters in the password: "))
letter = int(input ("Enter the total number of letters in the password: "))
c = random.choices(string.ascii_letters, k=letter)
number = int(input ("Enter the total number of numbers in the password: "))
d= random.choices(string.digits, k=number)
symbol = int(input ("Enter the total number of symbols in the password: "))
e= random.choices(string.punctuation, k=symbol)
if (len(c +d +e))  == total:
 c.extend(d)
 c.extend(e)
 random.shuffle(c)
 print (f" Generated Password: {"".join(c)}")
else:
 print (
    "invild input! the total number of characters is not equal with the entries "
    )