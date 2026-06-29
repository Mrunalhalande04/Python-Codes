Arr=[-10,-20,5,2]
mul=1
result=float('-inf')
ino=0
jno=0

for i in range(len(Arr)):
    for j in range(i+1,len(Arr)):
        mul=Arr[i]*Arr[j]

        if mul > result:
            ino=Arr[i]
            jno=Arr[j]
            result=mul

print(f"Maximum product pair is {ino} and {jno} and there product is {result}",)

