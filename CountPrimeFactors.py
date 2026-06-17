
class CountPrimeFact:
    def __init__(self,a):
        self.No=a

    def CountFact(self):
        num=self.No
        factor=[]
        divisor=2

        while num >1:
            while num % divisor==0:
                factor.append(divisor)
                num=num//divisor

            divisor=divisor+1

        print("Factors are ",factor)
            

def main():

    print("Enter Number")
    No=int(input())

    cobj=CountPrimeFact(No)

    cobj.CountFact()


if __name__=="__main__":
    main()