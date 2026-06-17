class PowerofThree:
    
    def __init__(self,a):
        self.No=a

    def PowerThree(self):

        return self.No>0 and 1162261467 % self.No==0

def main():

    print("Enter Number :")
    No=int(input())

    pobj=PowerofThree(No)

    ret=pobj.PowerThree()

    if ret==True:
        print("Power of Three")

    else:
        print("Not power of three")


if __name__ =="__main__":
    main()