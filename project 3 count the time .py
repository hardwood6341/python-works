total_second = int (input ("Please enter the number of seconds:\n"))
h = total_second //3600
remining_second = total_second % 3600
m= remining_second // 60 
s = remining_second % 60
print ("The total time of the course is" ,h,"hours and" ,m,"minuts and" ,s,"seconds")

#الغايه من هذا معرفه ال // و % 