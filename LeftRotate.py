#Left Rotate an Array by One Position
#3,4,5,1,2

Arr=[1,2,3,4,5]
k=2

for i in range(k):

    temp=Arr[0]
    for j in range(len(Arr)-1):
        Arr[j]=Arr[j+1]
 
    Arr[-1] = temp

for j in range(len(Arr)):
    print(Arr[j])