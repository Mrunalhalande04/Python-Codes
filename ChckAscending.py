
class Ascending():

    def __init__(self,A):
        self.Arrr=A

    def ChckAscending(self):
        Arr=self.Arrr
        bflag=True

        for i in range(len(Arr)):

            for j in range(i,len(Arr)-1,1):

                if(Arr[j] > Arr[j+1]):
                    bflag=False
                    return bflag
                
        return bflag
                
def main():

    print("Enter size")
    size=int(input())
    Brr=[]

    print("Enter elements ")

    for i in range(size):

        value=int(input())
        Brr.append(value)

    aobj=Ascending(Brr)

    bret=aobj.ChckAscending()

    if bret==True:
        print("List is in ascending order")

    else:
        print("Not in ascending order")

if __name__=="__main__":
    main()