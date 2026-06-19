
word="banana"
longest=""


for i in range(len(word)):
    for j in range(i,len(word)):
        substring=word[i:j+1]

        if substring==substring[::-1]:
            if len(substring) > len(longest):
                longest=substring


print("Longest substring :",longest)
print("Length of substring is:",len(longest))