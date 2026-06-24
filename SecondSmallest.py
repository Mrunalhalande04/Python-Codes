Arr=[10, 5, 20, 8, 15]
Min=Arr[0]
Smin=Arr[0]

for i in range(len(Arr)):
    if Arr[i] < Min:
        Smin=Min
        Min=Arr[i]

    elif Arr[i] < Smin and Arr[i] != Min:
        Smin=Arr[i]

print("Second Min :",Smin)
