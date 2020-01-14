class polynomial(object):
    def __init__(self,list):
        self.list = list # list is a collection of the coefficients of the polynomial P(x)
    def order(self):
        return (len(self.list)-1)
    def add(self,poly2):
        k = max(order(self.list),order(poly2))
        net = []
        for i in range(k):
            net.append(self.list[i] + poly2[i])
        return net
