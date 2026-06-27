Arr=[1,2,3,4,5]
Brr=[4,5,6,7,8]

print("Intersection of Two Array :")
for i in range(len(Arr)):
    for j in range(len(Brr)):
        if Arr[i]==Brr[j]:
            print(Arr[i])