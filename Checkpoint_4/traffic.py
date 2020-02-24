import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle #document pls
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
        def changes(road,c):
            k = []
            for i in range(len(road)):
                if(road[i] == 1):
                    k.append(i)
            j = 0
            for i in k:
                if c[i] == 0:
                    j += 1
            return j
        def eq(x):
            for i in range(1,len(x)):
                if x[i] == x[i-1]:
                    return i-1
        def movement(road):
            values = (0,0)
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
                    else: 
                        c[i] = 1
                elif (road[i] == 0):
                    if(i == 0 and road[k-1] == 1):
                        c[0] = 1
                        c[k-1] = 0
                    if(i > 0 and road[i-1] == 1):
                        c[i] = 1
                        c[i-1] = 0
            moved = changes(c,road)
            values = (c,moved)
            return values
        def display(arr):
            r = 0.4
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if(arr[i][j] == 1):
                        ax.add_patch(Circle((j,i),r,color='b'))
        arr[0] = self.road
        d = []
        for i in range(1,self.iterations):
            k = movement(self.road)
            N = k[0]
            avg_speed = k[1]/self.cars()
            self.road = N
            arr[i] = N
            d.append(avg_speed)
        print("equilbrium after {} iterations".format(eq(d)))
        display(arr)
        plt.axis('scaled')
        plt.show()
