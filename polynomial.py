class polynomial(object):
    def __init__(self,coeff):
        self.coeff = coeff # list is a collection of the coefficients of the polynomial P(x)
    def order(self):
        pos = 0
        for i in range(len(self.coeff)):
            if(self.coeff[i] !=0):
                pos = (i)
        return pos
    def add(self,polyB):
        k = min(polyB.order(),self.order())
        addition = []
        j = 0
        while (j<=k):
            addition.append(polyB.coeff[j]+self.coeff[j])
            j +=1
        if (polyB.order()>self.order()):
            addition.extend(polyB.coeff[j:])
        elif (polyB.order() < self.order()):
            addition.extend(self.coeff[j:])
        return addition
    
def main():
    p = polynomial([0,2,0,5])
    pB = polynomial([0,1,2,4,10])
    print(p.order())
    print(pB.order())
    print(p.add(pB))
main()