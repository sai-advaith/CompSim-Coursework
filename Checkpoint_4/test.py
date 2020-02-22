import numpy as np 
from traffic import Traffic
if __name__ == "__main__":
    road = np.array([0,1,0,1,1])
    iterations = int(input("number of require interations:"))
    ob = Traffic(road,iterations)
    ob.update()