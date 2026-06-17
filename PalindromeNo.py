class Palindrome:

    def __init__(self,a):
        self.No=a

    def PalindromeNo(self):

        digit=0
        num=self.No
        rev=0

        while num!=0:

            digit=num%10
            rev=rev*10+digit
            num=num//10

        if rev== self.No:
            return True
def main():

    print("Enter Number :")
    No=int(input())

    pobj=Palindrome(No)

    ret=pobj.PalindromeNo()

    if(ret==True):
        print("palindrome No")

    else:
        print("Not palindrome")



if __name__ =="__main__":
    main()