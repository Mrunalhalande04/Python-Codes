#Print every possible substring that can be formed from this string.

word="abc"

start=0
end=2

for i in range(len(word)):
    print(word[i])
    
    for j in range(i,len(word)-1):
        letter=word[start:end]
        print(letter)
        end=end+1
    start=start+1

