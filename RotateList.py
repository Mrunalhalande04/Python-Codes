#
# Rotate a list to the right by k

class Rotatet:

    def __init__(self,A):
        self.Arrr=A

    def RotateElement(self,k):
        Arr=self.Arrr
        n=len(Arr)

        for i in range(k):
            temp=Arr[n-1]

            for i in range(n-1,0,-1):
                Arr[i]=Arr[i-1]

            Arr[0]=temp

        print("Elements")
        print(Arr)

 
def main():

    print("Enter size of list :")
    size=int(input())

    print("Enter position")
    k=int(input())

    Brr=[]

    print("Enter elements :")

    for i in range(size):
        value=int(input())
        Brr.append(value)

    robj=Rotatet(Brr)

    robj.RotateElement(k)
    

    




if __name__=="__main__":
    main()