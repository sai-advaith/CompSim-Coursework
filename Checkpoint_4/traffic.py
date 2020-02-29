import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.patches import Circle #document pls
from random import randrange
class Traffic(object):
    def __init__(self,cars,road,iterations):
        """
        Constructor to initalize the class variables
        """
        self.road = road
        self.iterations = iterations
        self.cars = cars
        self.avg = []
    def movement(self):
        """
        Method to implement the movement of cars
        """
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
        k = len(self.road)
        moved = 0
        c = np.zeros(len(self.road)) #  this is to store the updated array
        for i in range(k):
            if (self.road[i] == 1):
                if (i < k - 1 and self.road[i+1] == 0):
                    c[i+1] = 1 #  if 1 then check if its not last and then update
                    c[i] = 0
                if (i == (k - 1) and self.road[0] == 0):
                    c[0] = 1 #  depending on whether its the last element or not
                    c[i] = 0
                else: 
                    c[i] = 1 #  keep it intact if one and no operations can be performed
            elif (self.road[i] == 0):
                if(i == 0 and self.road[k-1] == 1): 
                    c[0] = 1 # if zero check the previous and then move the last
                    c[k-1] = 0
                if(i > 0 and self.road[i-1] == 1):
                    c[i] = 1 #  if not the last and previous is 1, then move the previous element
                    c[i-1] = 0
        moved = changes(c,self.road) # this is to get the cars that moved
        return (c,moved) #  returning the tuple
    def equilbrium(self):
        """
        Helper method to check if steady state has been achieved
        """
        if (len(self.avg) <= 1):
            return self.avg[0]
        if (len(self.avg) == 2):
            if self.avg[1] == self.avg[0]:
                return self.avg[0]
            else:
                return self.avg[1]
        for i in range(1,len(self.avg)):
            if self.avg[i] == self.avg[i-1]: #  checking the previous and the current positions are the same
                return self.avg[i-1] #  returning the position once the previous and current items are the same
    def average(self):
        """
        Calculating the average velocity for the given road
        """
        result_tuple = self.movement()
        if (self.cars != 0):
            avg_speed = result_tuple[1] / self.cars
        else:
            avg_speed = 0 
        return avg_speed
    def update(self):
        """
        Updating the positions of the cars based on the algorithm given
        """
        N = np.zeros(len(self.road))
        arr = np.zeros(shape=(self.iterations,len(self.road)))
        ax = plt.axes()
    
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
        for i in range(1,self.iterations):
            k = self.movement() #  implementing the algorithm
            N = k[0] #  first element of the tuple is the updated positions of the car
            avg_speed = self.average()
            self.road = N #  updating the array
            arr[i] = N
            self.avg.append(avg_speed) #  storing all the average velocities in an array
        print("Average: ",self.equilbrium())
        display(arr) #  displaying the array
        plt.axis('scaled')
        plt.show()
    def generateDesnities(self):
        """
        Generating all the desnities
        """
        densities = []
        for i in range(len(self.road)+1): 
            densities.append(i/len(self.road))
        return densities
    def generateAverages(self):
        """
        Generating average velocities
        """
        def randomRoad(density):
            """
            Helper method to generate the random road
            """
            
            cars = density * len(self.road)
            i = 0
            road = [0]*len(self.road)
            while(i < cars):
                pos = randrange(len(road))
                if (road[pos] == 0):
                    road[pos] = 1
                    i+=1
            return road
        d = self.generateDesnities()
        averages = []
        for i in range(len(d)):
            self.road = randomRoad(d[i])
        return averages