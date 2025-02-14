# #first method
total_second = int (input ("Please enter the number of seconds:\n"))
h = total_second //3600
remining_second = total_second % 3600
m= remining_second // 60 
s = remining_second % 60
print ("The total time of the course is" ,h,"hours and" ,m,"minuts and" ,s,"seconds")

#الغايه من هذا معرفه ال // و % ❤️ 

# #second method
# total_seconds = int(input("please type the number of seconds : \n"))
# hours = total_seconds // 3600
# minuts = ((total_seconds) - (hours*3600)) // 60
# seconds = total_seconds % 60
# print("total time is " +  str(hours) + " hours " + str(minuts) + " minuts " + str(seconds) + " seconds ")

# #third method
# total_second = int (input ("Please enter the number of seconds:\n"))
# h = int (total_second / 3600)
# m= int (((total_second) - ( h *3600)) / 60) 
# s = (((total_second) - ( h *3600))- (m * 60))
# print ("The total time of the course is" ,h,"hours and" ,m,"minuts and" ,s,"seconds")

# # #fourth method
# total_second = int (input ("Please enter the number of seconds:\n"))
# h = total_second //3600
# m= (total_second % 3600) // 60 
# s = total_second  % 60
# print ("The total time of the course is" ,h,"hours and" ,m,"minuts and" ,s,"seconds")
