#project 15 profeshonal database
a = input ("Enter the name of a book you own: \n")
b = input ("Enter the name of another book you own (or press 'Enter' for skip): ")
library= []
library.append(a)
if b:
#هذا يعني اذا كانت هناك قيمه للمتغير عندها مشي البرنامج❤️
#اذا المستخدم ضغط انتر يعني تركه بدون قيمه ولن يمشي البرنامج❤️
#لا توجد الس لا نحتاجها❤️
  library.append(b)
print (f" your library :{library}")
c = input ("Enter the name of  book you wish to have in the future: ")
d= input ("Enter the name of another book you wish to have (or press 'Enter' to skip): ")
wishlist=[]
wishlist.extend([c,d])
if b == "" :
  wishlist.remove(b)
  print (f"you wishlist {wishlist}")
else:
  print (f"your wishlist {wishlist}")
e = input ("Enter the name of a book from your wishlist that you've acquired (or press 'Enter' to skip): ")
if e in wishlist:
  wishlist.remove(e)
  library.append(e)
  print (f"Updated Library :{library}")
  print (f"Updated Wishlist :{wishlist}")
else:
  print (f"Updated Library :{library}")
  print (f"Updated Wishlist :{wishlist}")

f = input ("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip): ")
if f in library:
  library.remove(f)

print (f"Final Library after Donation: {library}")
#هنا اعلاه ما يوجد ضمن حدود الـ(اف) يخضع لها وغيره لا❤️