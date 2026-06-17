class CollatzConjecture:

    def __init__(self,n):
        self.No=n


    def Collatz(self):
        num=self.No
        icount=0

        while num !=1:

            if num %2==0:
                icount=icount+1
                num=num/2

            elif num %2 ==1:
                icount=icount+1
                num=num*3+1

        return icount

def main():

    print("Enter Number :")
    No=int(input())

    cobj=CollatzConjecture(No)

    ret=cobj.Collatz()

    print("Steps are :",ret)


if __name__ =="__main__":
    main()