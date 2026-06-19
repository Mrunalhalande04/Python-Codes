#Longest substring without repeats starting from a specific index

word="abcdec"
index=3
brr=[]

for element in word[2:]:
    if element not in brr:
        brr.append(element)
        print(element)

        


