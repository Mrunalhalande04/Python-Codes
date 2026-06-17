class DuplicateElements:

    def __init__(self,A):
        self.Arrr=A

    def RemoveDuplicate(self):

        Arr=self.Arrr
        Result=[]

        for elements in Arr:
            if elements not in Result:
                Result.append(elements)

        
        print("List after removing duplicate elements :")
        for i in range(len(Result)):
            print(Result[i])




def main():
    
    print("Enter size of list ")
    size=int(input())

    Brr=[]

    print("Enter Elements :")

    for i in range(size):
        value=int(input())
        Brr.append(value)

    dobj=DuplicateElements(Brr)

    dobj.RemoveDuplicate()


    

if __name__ =="__main__":
    main()