#All substrings of length 2

word="abcd"

start=0
end=2

for i in range(len(word)-1):
    letter=word[start:end]
    print(letter)
    start=start+1
    end=end+1
