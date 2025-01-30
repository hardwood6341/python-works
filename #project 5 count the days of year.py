#project 5 count the days of year

#first method
t_days = int (input ("the number of days? \n"))
y = t_days // 360
m =(t_days % 360) // 30
w = (t_days % 30) // 7
d = (t_days % 30) % 7
print  (f"It's composed of:  ({y} years and {m} months and {w} weeks and {d} days)")

#second method
# t_days = int (input ("the number of days? \n"))
# y = int (t_days / 360)
# m = int (((t_days)-(y*360)) / 30)
# w = int ((((t_days)-(y*360)) - (m*30)) / 7)
# d = int ((((t_days)-(y*360)) - (m*30)) - (w*7))
# print  (f"It's composed of:  ({y} years and {m} months and {w} weeks and {d} days)")