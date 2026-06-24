Arr=[2,4,2,4,6,7,6,1,8]
icount=0

print("Duplicate element ")
for i in range(len(Arr)):

    found=False

    for j in range(i):
        if Arr[i]==Arr[j]:
            found=True
            break


    if found:
        continue

    duplicate=False

    for j in range(i+1,len(Arr)):
        if Arr[i]==Arr[j]:
            duplicate=True
            break
    
    if duplicate:
        print(Arr[i])
            
    