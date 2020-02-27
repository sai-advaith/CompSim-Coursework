import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle #document pls
class Traffic(object):
    def __init__(self,cars,road,iterations):
        """
        Constructor to initalize the class variables
        """
        self.road = road
        self.iterations = iterations
        self.cars = cars
    def update(self):
        """
        Updating the positions of the cars based on the algorithm given
        """
        N = np.zeros(len(self.road))
        arr = np.zeros(shape=(self.iterations,len(self.road)))
        ax = plt.axes()
        def changes(road,c):
            """
            Helper method to determine the number of cars that moved
            """
            k = []
            for i in range(len(road)):
                if(road[i] == 1):
                    k.append(i)
            j = 0 #  initially the cars moved are zero 
            for i in k:
                if c[i] == 0: #  comparing it with initial positions of the car
                    j += 1
            return j #  returning the number of cars that moved
        def equilbrium(x):
            """
            Helper method to check if steady state has been achieved
            """
            if (len(x) <= 1):
                return 0
            if (len(x) == 2):
                if x[1] == x[0]:
                    return 0
                else:
                    return 1
            for i in range(1,len(x)):
                if x[i] == x[i-1]: #  checking the previous and the current positions are the same
                    return i-1 #  returning the position once the previous and current items are the same
        def movement(road):
            """
            Helper method to implement the movement of cars
            """
            k = len(road)
            moved = 0
            c = np.zeros(len(road)) #  this is to store the updated array
            for i in range(k):
                if (road[i] == 1):
                    if (i < k - 1 and road[i+1] == 0):
                        c[i+1] = 1 #  if 1 then check if its not last and then update
                        c[i] = 0
                    if (i == (k - 1) and road[0] == 0):
                        c[0] = 1 #  depending on whether its the last element or not
                        c[i] = 0
                    else: 
                        c[i] = 1 #  keep it intact if one and no operations can be performed
                elif (road[i] == 0):
                    if(i == 0 and road[k-1] == 1): 
                        c[0] = 1 # if zero check the previous and then move the last
                        c[k-1] = 0
                    if(i > 0 and road[i-1] == 1):
                        c[i] = 1 #  if not the last and previous is 1, then move the previous element
                        c[i-1] = 0
            moved = changes(c,road) # this is to get the cars that moved
            return (c,moved) #  returning the tuple
        def display(arr):
            """
            Helper method to display the cars
            """
            r = 0.4
            for i in range(len(arr)):
                for j in range(len(arr[i])):
                    if(arr[i][j] == 1): #  if the position is occupied, then move the car
                        ax.add_patch(Circle((j,i),r,color='b'))
        arr[0] = self.road #  initial position of the cars in a 2d array
        d = [] #  storing the average speeds
        for i in range(1,self.iterations):
            k = movement(self.road) #  implementing the algorithm
            N = k[0] #  first element of the tuple is the updated positions of the car
            if (self.cars != 0):
                avg_speed = k[1]/self.cars #  returning the average based on the number moved
            else:
                avg_speed = 0
            self.road = N #  updating the array
            arr[i] = N
            d.append(avg_speed) #  storing all the average velocities in an array
        print("equilbrium after {} iterations".format(equilbrium(d))) #  printing equilibrium message
        display(arr) #  displaying the array
        plt.axis('scaled')
        plt.show()
