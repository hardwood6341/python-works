#project 8 use متداخله (nested IF)

country = input (" Are you Iraqi? (yes or no)\n").lower()
if  country == "yes" : 
  print ("Ok great, go to the next step..")
  age = int ( input ("what is  your age, Please?\n"))
  if age >= 18 :
    print ("you can have ID")
  else:
    print ( f"Sorry, {age} years old its too young")
else :
  print ("Sorry, its only for Iraqi")
    
#  مع المدخل من اليدايه   (lower)  الفكره الاولئ استخدام  ❤️
# الفكره الثانيه استخدام شرط اذا لم يتحقق فشل ما دونه ❤️