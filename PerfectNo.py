class PerfectNumber:

    def __init__(self,n):
        self.No=n

    def Perfect(self):
        num=self.No
        add=0
        

        for i in range(1,num,1):

            if num % i ==0:
                add=add+i

        return add==num

        


def main():

    print("Enter number ")
    No=int(input())

    pobj= PerfectNumber(No)

    ret=pobj.Perfect()

    if ret==True:
        print("Perfect number:")

    else:
        print("Not perfect number:")





if __name__ == "__main__":
    main()