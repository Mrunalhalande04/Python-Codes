#Build a substring until you hit a repeat

word="abcabc"
Brr=[]

for element in word:

    if element not in Brr:
        Brr.append(element)
        print(element)

    
