Arr=[1,5,7,-1,5]
target=6

print("All Pairs Given Sum :")
for i in range(len(Arr)):
    for j in range(i+1,len(Arr)):
        if Arr[i]+Arr[j]==target:
            for m in range(j):
                if Arr[j] != Arr[m]:
                 print(Arr[i],Arr[j])