#Pick the longest one out of all those results


word="pwwkew"
count=0
brr=[]
crr=[]
max=0


for i in range(len(word)):
    icount=0
    Brr=[]
    for element in word[i:]:
        if element not in Brr:
            Brr.append(element)
            icount=icount+1

        else:
            break

    crr.append(icount)

for i in range(len(crr)):

    if(crr[i]>max):
        max=crr[i]

print("Maximum length is :",max)



        



