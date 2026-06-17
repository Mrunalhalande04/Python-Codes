class MoveZeroEnd:

    def __init__(self,A):
        self.Arrr=A

    def ZerosEnd(self):
        Arr=self.Arrr
        Brr=[]
        icount=0

        for i in range(len(Arr)):
            if Arr[i]==0:
                icount=icount+1

        for i in range(len(Arr)):
            if Arr[i]!=0:
                Brr.append(Arr[i])

        for i in range(icount):
            Brr.append(0)


        print("Elements are ")
        for i in range(len(Brr)):
            print(Brr[i])



def main():

    print("Enter size of list :")
    size=int(input())

    Brr=[]

    print("Enter elements ")

    for i in range(size):
        value=int(input())
        Brr.append(value)


    mobj=MoveZeroEnd(Brr)

    mobj.ZerosEnd()

    
if __name__ =="__main__":
    main()