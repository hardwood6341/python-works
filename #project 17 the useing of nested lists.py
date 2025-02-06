#project 17 the useing of nested lists
fruits = [['apples','Bananas'],['coffee','milk','tea'] ]
print (fruits)
x = input ("Press enter to change the content ...")
if x == "":
    fruits[0].insert(0,'Oranges')
    fruits[0].insert(3, 'kiwis')
    fruits[1].insert(3,'water')
    fruits.insert(2,[1,2,3])
    fruits[1].remove('tea')
    fruits.append(['red','blur','black'])
    fruits[1].extend(fruits[3])
    print ("""here is the update of the list:
           
    """,fruits)
else:
    print ("what the fuck of you do!!")
