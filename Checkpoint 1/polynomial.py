class Polynomial(object):
    def __init__(self,coeff):
        self.coeff = coeff
# all functions except the first one return an object, which can be easily used to reference to other methods while testing
    def order(self):
        """
        The purpose of this function is to determine the order of a polynomial and return it as an integer
        """
        order = 0 # the coefficient is taken as zero if the variable does not appear in the equation
        for i in range(len(self.coeff)):
            if(self.coeff[i] !=0):
                order = (i) # order is based on the position of the last appearance of a non zero coefficient
        return order 

    def add(self,polyB):
        """
        Adding two polynomials and returning it as an object
        """
        k = min(polyB.order(),self.order()) # the addition will take place only till the length of the smaller list
        addition = Polynomial([]) # object will be returned from this method    
        j = 0
        if (k != 0): # case when the list is empty
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
        Calculating the derivative of a polynomial and returning its derivative as an object
        """
        diff = Polynomial([])
        if (len(self.coeff) > 1): # preventing cases where the list is empty or has only constant terms
            for i in range(1,len(self.coeff)):
                (diff.coeff).append((self.coeff[i]*(i))) # constant term of a polynomial will be zero after differentiating the polynomial
        else:
            diff.coeff.append(0)
        return diff

    def integrate(self,c):
        """
        Calculating the anti-derivative of a function and returning its integral as an object
        """
        integrate = Polynomial([c]) # constant term will be supplied to the method
        for i in range(len(self.coeff)):
            (integrate.coeff).append((self.coeff[i])/(i+1))
        return integrate 

    def __str__(self):
        """
        Representing a polynomial object as a string
        """
        s = ""
        if (len(self.coeff) == 1):
            return str(self.coeff[0])
        elif (len(self.coeff) < 1): 
            return str(0) # handling the case where the list is empty
        elif (self.coeff[0] != 0):
            s = str(self.coeff[0])
        
        for i in range(1,len(self.coeff)):
            if (self.coeff[i] < 0):
                s = s + " - " + str(abs(self.coeff[i])) + "x" + str(i) # to prevent problems with sign different cases have been created for negative and positive numbers
            elif (self.coeff[i] > 0 and s!= ""):
                s = s + " + " + str(abs(self.coeff[i])) + "x" + str(i)
            elif (self.coeff[i] > 0):
                s = s + str(abs(self.coeff[i])) + "x" + str(i)
        # this method avoids variables which do not appear in the polynomial.
        return s