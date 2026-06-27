Arr=[1,2,5,6]
no=0

print("Missing number are :")
for i in range(len(Arr)-1):
    if Arr[i]+1!=Arr[i+1]:
        for j in range(Arr[i]+1,Arr[i+1]):
            print(j)


        
