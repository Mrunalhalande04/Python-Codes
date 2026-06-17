class ReverseInteger:

    def __init__(self,n):
        self.No=n
    
    def Reverse(self):
        digit=0
        num=self.No
        sign=1
        rev=0

        if num < 0:
            sign=-1
            num=-num

        while num!=0:
            digit=num%10
            rev=rev*10+digit
            num=num//10

        rev=rev*sign

        print("Reverse number is :",rev)

def main():

    print("Enter number ")
    No=int(input())

    robj=ReverseInteger(No)

    robj.Reverse()



if __name__ =="__main__":
    main()