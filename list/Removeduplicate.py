list = [3,5,2,7,5,8,3,4,8,9,4,3,6]
print("UnOrdered List :",list)

result=[]

for i in list:
    if i not in result:
        result.append(i)
        result.sort()
print("Result List :",result)