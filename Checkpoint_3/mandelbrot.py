import numpy as np 
import cmath
import matplotlib.pyplot as plt
class Mandelbrot(object):
    def __init__(self,width,height,xlow,xhigh,ylow,yhigh):
        """
        Constructor
        """
        self.width = width # width of the grid
        self.height = height # height of the grid
        self.grid = np.zeros(shape = (width,height)) # initializing a grid of zeros
        self.xs = np.linspace(xlow,xhigh,width) # numpy array with high and low values initialized for a width for x axis. This forms the real axis
        self.ys = np.linspace(ylow,yhigh,height) # numpy array with high and low values initialized for a width for y axis. This forms the imaginary axis
    def check_mandel(self,c):
        """
        Checking the mandelbrot algorithm
        """
        z = 0 # inital value of z
        N = 0 # value of N to be plotted
        while (N < 255): 
            z = z**2 + c # iterative algorithm for the mandelbrot set
            if (abs(z) > 2):
                return N # returning the value if it isnt a mandelbrot
            N += 1 
        return 0 #returning zero after threshold is crossed
    def plot_mandel(self):
        """
        Plotting the values based on the iterative algorithm
        """
        for i in range(self.height):
            for j in range(self.width):
                c = complex(self.xs[j],self.ys[i]) # creating a complex number
                N = self.check_mandel(c) # the value after which the threshold for mandelbrot is crossed
                self.grid[i,j] = N # grid coordinates
        plt.imshow(self.grid, extent=(self.xs[0],self.xs[len(self.xs) - 1],self.ys[0],self.ys[len(self.ys) - 1])) # imshow to plot the points
        plt.show() # displaying
                
                


