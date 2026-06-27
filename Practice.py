Arr=[1,-2,3,-8]



for j in range(len(Arr)):
    if Arr[j-1] <0:
        for n in range(j,len(Arr)-1):
            if Arr[j] <0:
                temp=Arr[j]
                Arr[j]=Arr[j+1]
                Arr[j+1]=temp



print("Array after alternative :")
print(Arr)


