import numpy as np 
import matplotlib.pyplot as plt 
from mandelbrot import Mandelbrot
if __name__ == "__main__":
    """
    Main method
    """
    test = Mandelbrot(500,500,-2.025,0.6,-1.125,1.125) #mandelbrot object
    test.plot_mandel() # accessing the plotting method
   

