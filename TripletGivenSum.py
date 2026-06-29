Arr=[1,4,45,6,10,8]
no=22
ans=0

for i in range(len(Arr)):
  for j in range(i+1,len(Arr)):
     for k in range(j+1,len(Arr)):
        if Arr[i]+Arr[j]+Arr[k] == no:
         print(f"[{Arr[i]} , {Arr[j]} , {Arr[k]} ]")