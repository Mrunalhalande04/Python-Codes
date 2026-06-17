
class MergeTwoLists:

    def __init__(self,A,D,S):
        self.Arrr=A
        self.Drrr=D
        self.size=S

    def MergeTwo(self):
        s=self.size
        Arr=self.Arrr
        Drr=self.Drrr
        Brr=[]

        for element in Arr:
            if element not in Brr:
                Brr.append(element)

        for element in Drr:
            if element not in Brr:
                Brr.append(element)


        print("Combined elements of both list :")
        for i in range(len(Brr)):
            print(Brr[i])


def main():

    print("Enter size of list :")
    size=int(input())

    Brr=[]
    Crr=[]

    print("Enter first list elements :")
    for i in range(size):
        value=int(input())
        Brr.append(value)

    print("Enter second list elements :")
    for i in range(size):
        value=int(input())
        Crr.append(value)

    mobj=MergeTwoLists(Brr,Crr,size)

    mobj.MergeTwo()



if __name__=="__main__":
    main()