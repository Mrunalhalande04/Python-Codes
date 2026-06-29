Arr=[2,3,10,6,4,8,1]
max=float('-inf')

for i in range(len(Arr)):
    ans=0
    for j in range(i+1,len(Arr)):
        ans=Arr[j]-Arr[i]

        if ans > max:
            max=ans
    
print("Maximum number is :",max)
