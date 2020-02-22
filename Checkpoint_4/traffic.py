import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle 
class Traffic(object):
    def __init__(self,road,iter):
        self.road = road
        self.iterations = iter
    
    def update(self):
        N = np.zeros(len(self.road))
        arr = np.zeros(shape=(self.iterations,len(self.road)))
        ax = plt.axes()
        r = 0.4
        def movement(road):
            k = len(road)
            c = np.zeros(len(road))
            for i in range(k):
                if (road[i] == 1):
                    if (i < k - 1 and road[i+1] == 0):
                        c[i+1] = 1
                        c[i] = 0
                    elif (i == (k - 1) and road[0] == 0):
                        c[0] = 1
                        c[i] = 0
                    else: 
                        c[i] = 1
                elif (road[i] == 0):
                    if(i == 0 and road[k-1] == 1):
                        c[0] = 1
                        c[k-1] = 0
                    elif(i > 0 and road[i-1] == 1):
                        c[i] = 1
                        c[i-1] = 0
            return c
        def display(arr):
            r = 0.4
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if(arr[i][j] == 1):
                        ax.add_patch(Circle((j,i),r,color='y'))
        for i in range(self.iterations):
            N = movement(self.road)
            self.road = N
            arr[i] = N    
        display(arr)
        plt.axis('scaled')
        plt.show()
