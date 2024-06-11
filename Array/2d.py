region_list = [

    ["US","Canada"],
    ["India", "China"],
    ["UK", "Germanay"]

]


print(region_list)

for i in region_list:
    for j in i:
        print(j)

print("******************")

# It prints Germany
region_list[2][1]

print(region_list[2][1])