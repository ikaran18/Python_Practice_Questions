list = [3,5,2,7,5,8,3,4,8,9,4,3,6]
print("UnOrdered List :",list)

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]>=list[j]:
            list[i],list[j]=list[j],list[i]
print("Ordered List :",list)