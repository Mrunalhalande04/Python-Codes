class TargetElement:

    def __init__(self,A):
        self.Arrr=A

    def SearchElement(self,No):

        Arr=self.Arrr

        for i in range(len(Arr)):
            if Arr[i]==No:
                return i
        
        return -1


def main():
    
    print("Enter size of list ")
    size=int(input())

    print("Enter element to search :")
    val=int(input())

    Brr=[]

    print("Enter Elements :")

    for i in range(size):
        value=int(input())
        Brr.append(value)

    tobj=TargetElement(Brr)

    ret=tobj.SearchElement(val)

    print("index",ret)

if __name__ =="__main__":
    main()