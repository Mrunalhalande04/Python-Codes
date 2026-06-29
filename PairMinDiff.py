Arr=[10,22,28,29,30,40]
result=float('inf')
Min=[]
ino=0
jno=0

for i in range(len(Arr)):
    
    for j in range(i+1,len(Arr)):
        ans=Arr[j]-Arr[i]

        if ans < result:
            ino=Arr[i]
            jno=Arr[j]
            result=ans


print(f"Minimum number pair is {ino}  and {jno} diff is {result} ")

    



    

