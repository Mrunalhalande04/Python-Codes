# Check if a string has any repeating characters

word="abcdefb"
Brr=[]
Flag=False


for element in word:

    if element not in Brr:
        Brr.append(element)

    else:
        Flag=True


if Flag==True:
    print("Repeatation Occurs ")

else:
    print("No Repeatation :")
        