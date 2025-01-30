#first method
Length = input ("Please type Length : \n")
Width = input ("Please type Width : \n")
Price = input (" how much for 1 meter? \n")
print (" total erae is :" , (float (Length) * float (Width)))
print (" Give the guy :",((float (Length)* float (Width)) * (float (Price)) ))

# هنا الشيء المهم انه يمكن في حالة وضع فارزه ان نجعل 
#print يطبع اكثر من نوع داتا

#second method
x = input (" what is the length? \n")
y = input (" what is the width? \n")
total_area =  float (x)  * float (y)
print ("total area is : ", (total_area))
z = float (input (" what is the price for 1 meter, you want to pay? \n"))
print (" Give the guy:", total_area * z ,"$" )
