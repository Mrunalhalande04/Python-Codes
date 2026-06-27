Arr=[1,2,3,4,1]
start=0
end=len(Arr)-1
flag=True

while(start < end):

    if Arr[start] != Arr[end]:
        flag=False
        break

    start=start+1
    end=end-1


if flag==True:
    print("Palindrome")

else:
    print("Not Palindrome")
    