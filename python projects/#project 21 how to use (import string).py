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