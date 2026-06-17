class LCMGCDNumber:

    def __init__(self,n1,n2):
        self.No1=n1
        self.No2=n2
    
    def GCD(self):

        a=self.No1
        b=self.No2
        num=0

        while(b !=0):
            num=a%b
            a=b
            b=num
            num=0
            
        return a
    
    def LCM(self):

        a=self.No1
        b=self.No2
        GCDNo=self.GCD()
        LCM=0

        LCM=a*b/GCDNo

        print("LCM is",LCM)
        print("GCD is",GCDNo)
        

"remianing"

def main():

    print("Enter number ")
    No1=int(input())

    print("Enter number ")
    No2=int(input())

    robj=LCMGCDNumber(No1,No2)

    robj.LCM()


if __name__ =="__main__":
    main()