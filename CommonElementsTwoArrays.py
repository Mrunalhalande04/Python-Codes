Arr=[2,3,4,5,6,9]
Brr=[3,6,9,1,7]

print("Common Elements in Two Arrays are :")
for i in range(len(Arr)):

    for j in range(len(Brr)):

        if Arr[i]==Brr[j]:
            print(Arr[i])

