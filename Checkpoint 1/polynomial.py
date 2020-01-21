class polynomial(object):
    def __init__(self,coeff):
        self.coeff = coeff
# all functions except the first one return an object, which can be easily used to reference to other methods while testing
    def order(self):
        """
        The purpose of this function is to determine the order of a polynomial and return an integer
        """
        order = 0 # the coefficient is taken as zero if the variable does not appear in the equation
        for i in range(len(self.coeff)):
            if(self.coeff[i] !=0):
                order = (i) # order is based on the position of the last appearance of a non zero coefficient
        return order # order of the equation

    def add(self,polyB):
        """
        Adding two polynomials and returning an object which is the result of addition of two polynomials
        """
        k = min(polyB.order(),self.order()) # the addition will take place only till the length of the smaller list
        addition = polynomial([]) # object will be returned from this method
        j = 0
        while (j<=k):
            (addition.coeff).append(polyB.coeff[j]+self.coeff[j])
            j +=1
        if (polyB.order()>self.order()):
            (addition.coeff).extend(polyB.coeff[j:])
        elif (polyB.order() < self.order()):
            (addition.coeff).extend(self.coeff[j:]) # we will append the list from the difference of the orders
        return addition

    def differentiate(self):
        """
        Calculating the derivative of a polynomial and returning an object containing the derivative of a polynomial
        """
        diff = polynomial([])
        for i in range(1,len(self.coeff)):
            (diff.coeff).append((self.coeff[i]*(i))) # constant term will become zero in the derivative 
        return diff

    def integrate(self,c):
        """
        Calculating the anti-derivative of a function and returning an object containing its integral.
        """
        integrate = polynomial([]) # constant term will be supplied to the method
        for i in range(len(self.coeff)):
            (integrate.coeff).append((self.coeff[i])/(i+1))
        return integrate 

    def strForm(self):
        """
        Representing a polynomial as a string
        """
        s = str(self.coeff[0]) 
        for i in range(1,len(self.coeff)):
            if (self.coeff[i] < 0):
                s = s + " - " + str(abs(self.coeff[i])) + "x" + str(i) # to prevent problems with sign different cases have been created for negative and positive numbers
            elif (self.coeff[i] > 0):
                s = s + " + " + str(abs(self.coeff[i])) + "x" + str(i)
        # this method avoids variables which do not appear in the polynomial.
        return s