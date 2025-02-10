# input: ali ahmed, yasser alwan, mouhamed hasan
a = input("Enter the first and last name of your friends separated by comma:").split(", ")
# output ['ali ahmed', 'yasser alwan', 'mouhamed hasan']
for name in a:
    x = name.split(" ")
    # output ['ali', 'ahmed']
    #  ['yasser', 'alwan']
t applying     #  ['mouhamed', 'hasa']
    s = [] 
    b = []
    for part in x:
        s.append(part.capitalize())
    print(s)

# output ['
#ali', 'ahmed', 'yasser', 'alwan', 'mouhamed', 'hasan']
# print (result)
# # ali ahmed, yasser alwan, mouhamed hasa