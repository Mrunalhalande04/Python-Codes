Arr=[5,-3,9,2,1,-3]
temp=0

for i in range (len(Arr)):
     for j in range(i,len(Arr)):

        if Arr[j] < 0 :
            temp=Arr[j]
            Arr[j]=Arr[j-1]
            Arr[j-1]=temp


print("Moved All Negative Numbers to the Beginning")
for item in Arr:
    print(item)



    
