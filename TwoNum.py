
class TwoNum:

    def __init__(self,A):
        self.Arrr=A

    def TwoNumber(self,target):
        Arr=self.Arrr

        for i in range(len(Arr)-1):

            if Arr[i]+Arr[i+1]==target:
                print("Index Values are :",i,i+1)
                

def main():

    print("Enter size ")
    size=int(input())

    print("Enter Target Number ")
    target=int(input())

    Brr=[]
    print("Enter Elements :")

    for i in range(0,size):
        value=int(input())
        Brr.append(value)

    tobj=TwoNum(Brr)

    tobj.TwoNumber(target)


if __name__ =="__main__":
    main()