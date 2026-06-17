class SecondLargest:

    def __init__(self,A):
        self.Arrr=A

    def SecondLarge(self):

        Arr=self.Arrr
        Max=Arr[0]
        Smax=float('-inf') #0

        for i in range(len(Arr)):

            if Arr[i] > Max:
                Smax=Max
                Max=Arr[i]

            elif Arr[i] > Smax and Arr[i] != Max:
                Smax = Arr[i]

        return Smax

def main():
    
    print("Enter size of list ")
    size=int(input())

    Brr=[]

    print("Enter Elements :")

    for i in range(size):
        value=int(input())
        Brr.append(value)

    sobj=SecondLargest(Brr)

    ret=sobj.SecondLarge()

    print("Second Largest Element is :",ret)
    


    

if __name__ =="__main__":
    main()