
class HappyNo:

    def __init__(self,a):
        self.No=a


    def Power(self,digit):
        digit=digit
        return digit*digit

    def Happy(self):

        digit=0
        flag=False
        Add=0
        Num=self.No

        
        while Num>9:
            Add=0
            while Num !=0:
                digit=Num%10
                Add=Add+self.Power(digit)
                Num=Num//10

            Num=Add
     
        if(Num==1):
            flag=True
            return flag

def main():
    
    print("Enter Number :")
    No=int(input())

    hobj=HappyNo(No)
    ret=hobj.Happy()

    if(ret==True):
        print("Happy No")

    else:
        print("Not happy No")

if __name__=="__main__":
    main()

