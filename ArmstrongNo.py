class Armstrong:

    def __init__(self,n):
        self.No=n


    def Count(self,No):

        count=0

        while No!=0:
            count=count+1
            No=No//10

        return count


    def Power(self,base,expo):
        pow=1
        
        for i in range(1,expo+1,1):
            pow=pow*base

        return pow



    def ArmstrongNo(self):
        num=self.No
        Noi=self.No
        digit=0
        add=0
        count=self.Count(num)

        while num!=0:
            digit=num%10
            add=add+self.Power(digit,count)
            num=num//10

        return add==Noi



def main():

    print("Enter Number :")
    No=int(input())

    aobj=Armstrong(No)

    ret=aobj.ArmstrongNo()

    if ret==True:
        print("Armstrong Number :")

    else:
        print("Not Armstrong Number :")


if __name__ =="__main__":
    main()