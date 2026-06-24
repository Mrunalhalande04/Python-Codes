
no=[1,2,3]
print("j is ")
for i in range(len(no)):
    for j in range(i+1,len(no)-1):
        sum=no[i]+no[j]
        print(sum)