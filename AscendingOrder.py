
class AscendingOrder:

    def __init__(self,A):
        self.Arrr=A

    def Ascending(self):
        Arr=self.Arrr

        for i in range(len(Arr)):
            for j in range(i,len(Arr)-1,1):
                
                if Arr[j] > Arr[j+1]:

                    temp=Arr[j]
                    Arr[j]=Arr[j+1]
                    Arr[j+1]=temp

        print("Elements after sorting in ascending")
        for i in range(len(Arr)):
            print(Arr[i])

def main():

    print("Enter size of list :")
    size=int(input())

    Brr=[]
    
    print("Enter elements :")
    for i in range(size):
        value=int(input())
        Brr.append(value)


    aobj=AscendingOrder(Brr)

    aobj.Ascending()

    





if __name__ =="__main__":
    main()