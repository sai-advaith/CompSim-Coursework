import numpy as np 
from traffic import Traffic
from random import randrange
if __name__ == "__main__":
    size = int(input("size of the road: "))
    road = np.zeros(shape=size)
    density = float(input("density of the road: "))
    iterations = int(input("number of require interations:"))
    cars = size*density
    i = 0
    while(i<cars):
        pos = randrange(len(road))
        if (road[pos] == 0):
            road[pos] = 1
            i+=1
    tr = Traffic(cars,road,iterations)
    tr.update()
