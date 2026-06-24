Arr=[-5,-8,-2,-10]

Max=Arr[0]
Min=Arr[0]
diff=0


for i in range(0,len(Arr)):
    if Arr[i] > Max:
        Max=Arr[i]

    elif Arr[i] < Min :
        Min=Arr[i]


diff=Max-Min

print("Difference is ",diff)
