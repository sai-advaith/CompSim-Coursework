class polynomial(object):
    def __init__(self,coeff):
        self.coeff = coeff # list is a collection of the coefficients of the polynomial P(x)
    def order(self):
        pos = 0
        for i in range(len(self.coeff)):
            if(self.coeff[i] !=0):
                pos = (i)
        return pos
def main():
    p = polynomial([0,2,4,5])
    pB = polynomial([1,2,4,5])
main()