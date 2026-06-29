Arr=[1,3,5,2,2]


for i in range(len(Arr)):
    left=0
    right=0

    for j in range(i):
        left=left+Arr[j]

    for j in range(i+1,len(Arr)):
        right=right+Arr[j]

    if left==right:
        print("Equilibrium Index is :",i)


