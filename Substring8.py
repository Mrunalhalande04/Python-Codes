# Run question 7 for every starting index

word="abcabc"
Brr=[]

for i in range(len(word)):
    Brr=[]
    for element in word[i:]:

        if element not in Brr:
            Brr.append(element)
            print(element)

