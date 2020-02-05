import numpy as np 
import cmath
import matplotlib.pyplot as plt
class Mandelbrot(object):
    def __init__(self,width,height,xlow,xhigh,ylow,yhigh):
        self.width = width
        self.height = height
        self.grid = np.zeros(shape = (width,height))
        self.xs = np.linspace(xlow,xhigh,width)
        self.ys = np.linspace(ylow,yhigh,height)
    # def __str__(self):
    #     s = ""
    #     for i in range(len(self.grid)):
    #         for j in range(len(self.grid[0])):
    #             s = s + str(self.grid[j][i])
    #         s = s + "\n"
    #     return s
    def check_mandel(self,c):
        z = 0
        N = 0
        while (N < 255):
            z = z**2 + c
            if (abs(z) > 2):
                return N
            N += 1
        return 0
    def plot_mandel(self):

        # keep passing x,y into the check_mandel function. complex(x,y)
        # run a loop across x and y 
        # initialzie it in the grid?
        for i in range(self.height):
            for j in range(self.width):
                c = complex(self.xs[j],self.ys[i])
                N = self.check_mandel(c)
                self.grid[i,j] = N
        plt.imshow(self.grid, extent=(0,500,0,500))
        plt.show()
                
                


