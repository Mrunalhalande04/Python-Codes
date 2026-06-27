

Arr=[1,2,4,5,6]

print("Missing number is :")
for i in range(len(Arr)):
    if Arr[i]+1 != Arr[i+1]:
        print(Arr[i]+1)

                