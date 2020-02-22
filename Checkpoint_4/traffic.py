import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle 
class Traffic(object):
    def __init__(self,road,iter):
        self.road = road
        self.iterations = iter
    def cars(self):
        car = 0
        for i in self.road:
            if i == 1:
                car += 1
        return car
    def update(self):
        N = np.zeros(len(self.road))
        arr = np.zeros(shape=(self.iterations,len(self.road)))
        ax = plt.axes()
        values = (0,0)
        r = 0.4
        def movement(road):
            k = len(road)
            moved = 0
            c = np.zeros(len(road))
            for i in range(k):
                if (road[i] == 1):
                    if (i < k - 1 and road[i+1] == 0):
                        c[i+1] = 1
                        c[i] = 0
                    if (i == (k - 1) and road[0] == 0):
                        c[0] = 1
                        c[i] = 0
                    if(road[i] == 0):
                        moved+= 1
                    else: 
                        c[i] = 1
                elif (road[i] == 0):
                    if(i == 0 and road[k-1] == 1):
                        c[0] = 1
                        c[k-1] = 0
                    if(i > 0 and road[i-1] == 1):
                        c[i] = 1
                        c[i-1] = 0
                    if(road[i] == 1):
                        moved+=1    
                print(moved)            
            values = (c,moved)
            return values
        def display(arr):
            r = 0.1
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if(arr[i][j] == 1):
                        ax.add_patch(Circle((j,i),r,color='r'))
        for i in range(self.iterations):
            k = movement(self.road)
            N = k[0]
            print(k[1])
            avg_speed = k[1]/self.cars()
            self.road = N
            arr[i] = N
            # print(avg_speed)    
        display(arr)
        plt.axis('scaled')
        plt.show()
