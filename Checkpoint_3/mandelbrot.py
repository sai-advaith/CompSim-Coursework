import numpy as np 
import cmath
import matplotlib.pyplot as plt
class Mandelbrot(object):
    def __init__(self,width,height,xlow,xhigh,ylow,yhigh):
        self.width = width
        self.height = height
        self.x = (xlow,xhigh)
        self.y = (ylow,yhigh)
        self.grid = np.zeros(shape = (width,height))
        self.xs = np.linspace(self.x[0],self.x[1])
        self.ys = np.linspace(self.y[0],self.y[1])
    def __str__(self):
        s = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                s = s + str(self.grid[j][i])
            s = s + "\n"
        return s
    def check_mandel(self,c):
        z = 0
        N = 0
        while (N < 255):
            z = z**2 + c
            if (abs(z) > 2):
                break
            N += 1
        return N
        

