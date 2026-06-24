
class SlidingWindow:

    def __init__(self,A):
        self.Arrr=A

    def SlidingWindowMaximum(self,target):
        result=[]
        Arr=self.Arrr
        Max=0

        for i in range(len(Arr)-target+1):
            Max=Arr[i]
            for j in range(i,i+target):
                if Arr[j] > Max:
                    Max=Arr[j]
            result.append(Max)

        print("Elements")
        for item in result:
            print(item)


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

    tobj=SlidingWindow(Brr)

    tobj.SlidingWindowMaximum(target)


if __name__ =="__main__":
    main()