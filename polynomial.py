class polynomial(object):
    def __init__(self,list):
        self.list = list # list is a collection of the coefficients of the polynomial P(x)
    def printPoly(self):
        s = ""
        for i in range(len(self.list)):
            if (self.list[i] !=0 and i > 0):
                s = s + str(self.list[i])+"x"+str(i+1)+ "+ "
            elif (self.list[i]!= 0 and i == 0):
                s = s + str(self.list[i])
        return s
def main():
    p = polynomial([2,0,4,-1,6])
    print(p.printPoly())
main()