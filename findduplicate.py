#Find All Duplicates

class Duplicate:

    def __init__(self,A):
        self.Arrr=A

    def findduplicate(self):
        Arr=self.Arrr

        print("Duplicate elements are :")
        for i in range(len(Arr)):
            for j in range(i+1,len(Arr)-1):
                if Arr[i]==Arr[j]:
                    print(Arr[i])
                    break

def main():

    print("Enter size:")
    size=int(input())

    brr=[]

    print("Enter elements ")
    
    for i in range(size):
        value=int(input())
        brr.append(value)


    dobj=Duplicate(brr)

    dobj.findduplicate()

    






if __name__ =="__main__":
    main()