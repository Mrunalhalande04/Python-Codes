Arr=[2,3,1,6,3,2,1,9]
icount=0

for i in range(len(Arr)):

    found=False

    for j in range(i):
        if Arr[i]==Arr[j]:
            found=True
            break


    if found:
        continue

    icount=0

    for j in range(len(Arr)):
        if Arr[i]==Arr[j]:
            icount=icount+1

    print(f"Count of {Arr[i]} is {icount}")