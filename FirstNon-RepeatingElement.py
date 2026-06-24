
Arr=[10,5,3,4,3,5,6]
icount=0

for i in range(len(Arr)):
    icount=0
    for j in range(len(Arr)):
        if Arr[i]==Arr[j]:
            icount=icount+1

    if icount== 1:
        print(Arr[i])
        break
