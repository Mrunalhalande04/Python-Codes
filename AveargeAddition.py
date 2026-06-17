
class Calculation:

    def __init__(self,Ar,s):

        self.Arrr=Ar
        self.size=s

    def Summation(self):
        Add=0
        s=self.size
        Arr=self.Arrr

        for i in range(s):
            Add=Add+Arr[i]

        return Add
    
    def Average(self):
        icount=0
        s=self.size
        Add=self.Summation()
        Arr=self.Arrr

        for i in range(s):
            icount=icount+1

        return Add // icount ,Add


    

def main():
    print("Enter size of list")
    size=int(input())

    Brr=[]

    print("Enter Elements:")
    for i in range(size):

        value=int(input())
        Brr.append(value)

    print("Elements are :")
    for i in range(size):

        print(Brr[i])

    cobj=Calculation(Brr,size)

   

    aret,ret=cobj.Average()

    print(f"Average is {aret} & Addition is {ret} ")



if __name__ =="__main__":
    main()