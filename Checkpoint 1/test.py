from polynomial import polynomial
def main():
    polynomialA = polynomial([2,0,4,-1,0,6]) # representation of 2 + 4x^2 - x^3 + 6x^5
    polynomialB = polynomial([-1,-3,0,4.5]) # representation of -1 -3x + 4.5x^3
    #  if the variable does not appear in the polynomial then its coefficient is 0
    print("order of polynomialA is: ",polynomialA.order())
    print("addition of polynomialA and polynomialB is: ",polynomialA.add(polynomialB).strForm())
    print("first derivative of polynomialA is: ",polynomialA.differentiate().strForm())
    print("Antiderivative of polynomialA is: ", polynomialA.integrate(2).strForm())
main()