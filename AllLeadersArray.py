Arr=[16,17,4,3,5,2]
found=False

for i in range(len(Arr)):
    found=False
    for j in range(i+1,len(Arr)):
        if Arr[i] < Arr[j]:
            found=True
            break
    if found :
        continue

    if found==False:
        print(Arr[i])
    
            


            



