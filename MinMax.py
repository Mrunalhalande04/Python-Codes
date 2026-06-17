
class MinMax:

    def __init__(self,A,S):
        self.Brr=A
        self.size=S

    def Maximum(self):

        Arr=self.Brr
        max=Arr[0]
        s=self.size

        for i in range(s):

            if Arr[i] > max:
                max=Arr[i]

        return max
    
    def Minimum(self):

        Arr=self.Brr
        min=Arr[0]
        s=self.size

        for i in range(s):

            if Arr[i] < min:
                min=Arr[i]

        return min


def main():
    
    print("Enter size of list ")
    size=int(input())

    Brr=[]

    print("Enter Elements :")

    for i in range(size):
        value=int(input())
        Brr.append(value)


    mobj=MinMax(Brr,size)

    ret=mobj.Maximum()
    print("Maximum Number is :",ret)

    rret=mobj.Minimum()
    print("Minimum number is :",rret)

    





if __name__ =="__main__":
    main()