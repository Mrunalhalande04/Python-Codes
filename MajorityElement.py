Arr=[2,2,1,2,3,2,2]
found=False
icount=0
count=0
ino=0
no=0


for i in range(len(Arr)):
    for j in range(i):
        if Arr[i]==Arr[j]:
            found=True
            break

    if found:
        continue

    for j in range(i,len(Arr)):
        
        if Arr[i]==Arr[j]:
            icount=icount+1
            no=Arr[i]

    if icount > count:
        count=icount
        ino=no
    icount=0


ans=len(Arr)/2
if count > ans:
    print("Majority element is :",ino)





