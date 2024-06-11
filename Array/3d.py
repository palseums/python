region_list = [

   [[1,2,3],[4,5,6]],
   [[7,8,9],[10,11,12]]

]

for i in region_list:
    for j in i:
        for k in j:
            print(k)


# It prints 7
region_list[1][0][0]

print("*************")

print(region_list[1][0][0])
