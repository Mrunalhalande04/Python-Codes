Arr = [10,5,12,3,55,30,4,11,2]
brr=[]

for i in range(len(Arr)):
    for j in range(i):
        
        if Arr[i]+1==Arr[j] or Arr[i]-1 == Arr[j]:
            if Arr[j] not in brr:
                brr.append(Arr[j])
        

    for j in range(len(Arr)):
        if Arr[i]+1== Arr[j] or Arr[i]-1 == Arr[j]:
            if Arr[j] not in brr:
                brr.append(Arr[j])
        
print("Consu:")
print(brr)

