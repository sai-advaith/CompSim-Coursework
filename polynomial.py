class polynomial(object):
    def __init__(self,coeff):
        self.coeff = coeff
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
    def differentiate(self):
        diff = []
        for i in range(1,len(self.coeff)):
            diff.append((self.coeff[i]*(i)))
        return diff
    def integrate(self,c):
        integrate = [c]
        for i in range(len(self.coeff)):
            integrate.append((self.coeff[i])/(i+1))
        return integrate
def main():
    p = polynomial([2,0,0,10])
    pB = polynomial([0,1,2,4,10])
    print(p.integrate(10))
main()