#project 5 count the days of year

#first method
t_days = int (input ("the number of days? \n"))
y = t_days // 360
m =(t_days % 360) // 30
w = (t_days % 30) // 7
d = (t_days % 30) % 7
print  (f"It's composed of:  ({y} years and {m} months and {w} weeks and {d} days)")

#الفكرة ان ((//)) تستخدم لاخذ قسمة الرقم بدون باقي وال ((%)) تستخدم لاخذ الباقي ❤️
#  مثلا 7 تقسيم 6 الناتج واحد و مثلا 33 تقسيم 30 يساوي 3 ❤️

# second method
# t_days = int (input ("the number of days? \n"))
# y = int (t_days / 360)
# m = int (((t_days)-(y*360)) / 30)
# w = int ((((t_days)-(y*360)) - (m*30)) / 7)
# d = int ((((t_days)-(y*360)) - (m*30)) - (w*7))
# print  (f"It's composed of:  ({y} years and {m} months and {w} weeks and {d} days)")