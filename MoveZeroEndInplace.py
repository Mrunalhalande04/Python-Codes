class MoveZeroEnd:

    def __init__(self,A):
        self.Arrr=A

    def ZerosEnd(self):
        Arr=self.Arrr
        
    
        for i in range(len(Arr)):
            for j in range(0,len(Arr)-1):
                if Arr[j]==0:
                    temp=Arr[j]
                    Arr[j]=Arr[j+1]
                    Arr[j+1]=temp

        print("Elements are ")
        for i in range(len(Arr)):
            print(Arr[i])
        


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