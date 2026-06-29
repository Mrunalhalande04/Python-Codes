Arr=[1,2,3,4]
result=[]


for i in range(len(Arr)):
    mul=1
    for j in range(i):
        mul=mul*Arr[j]

    for j in range(i+1,len(Arr)):
        mul=mul*Arr[j]

    result.append(mul)

print(result)