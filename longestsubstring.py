#Longest Substring without repeating characters

class LongestSubstring:
    def __init__(self,W):
        self.word=W


    def longsubstring(self):

        words=self.word
        brr=[]
        icount=0

        for element in words:
            if element not in brr:
                brr.append(element)
                icount=icount+1

        print("Longest Substring without repeating characters is :")

        for i in range(len(brr)):
            print(brr[i])

        print("Count of Longest Substring without repeating characters is :",icount)



def main():

    print("Enter string:")
    word=input()

    lobj=LongestSubstring(word)

    lobj.longsubstring()


if __name__ =="__main__":
    main()