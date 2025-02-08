#codes 1 flattened list

#method 1
# b = [[1], [1,3,5]]
# flattened_list = [item for sublist in b for item in sublist]
# print(flattened_list)

#method 2
b = [[1], [1,3,5]]
flattened_list = []
for y in b:
    #هنا احنه راح نجي ع مجموعه مجموعه
    for x in y:
         #هنا احنه راح نجي ع المنت المنت
        flattened_list.append(x)
            #هنا ضفنا المنت المنت
print (flattened_list)