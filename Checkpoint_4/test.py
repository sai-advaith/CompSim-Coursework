import numpy as np 
from traffic import Traffic
from random import randrange
if __name__ == "__main__":
    """
    Main method
    """
    size = int(input("size of the road: "))
    road = np.zeros(shape=size)
    density = float(input("density of the road: "))
    iterations = int(input("number of require interations:"))
    cars = size*density
    i = 0
    while(i<cars):
        pos = randrange(len(road)) #  getting random position in the road
        if (road[pos] == 0): #  if the positions is zero then place the car there
            road[pos] = 1
            i+=1 #  increase car numbers placed
    tr = Traffic(cars,road,iterations) #  creating object
    tr.update() #  moving the car
