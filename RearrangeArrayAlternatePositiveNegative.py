Arr=[-9,6,1,3,-5,-2,9,]
positive=[]
negative=[]


for i in range(len(Arr)):
    if Arr[i] > 0:
        positive.append(Arr[i])

    elif Arr[i] < 0:
        negative.append(Arr[i])


result = []

for i in range(len(negative)):
    result.append(negative[i])
    result.append(positive[i])
print(result)



    