#Find the first character that repeats

word="abcda"

brr=[]


for element in word:
    
    if element in brr:
        print("First repeatating character",element)

    else:
        brr.append(element)

