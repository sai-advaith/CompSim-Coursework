import numpy as np 
import matplotlib.pyplot as plt
class Mandelbrot(object):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.grid = np.zeros(shape = (width,height))
    def __str__(self):
        s = ""
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                s = s + str(self.grid[i][j])
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
        

