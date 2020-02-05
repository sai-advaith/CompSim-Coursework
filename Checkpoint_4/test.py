import numpy as np 
from traffic import Traffic
if __name__ == "__main__":
    N = 1
    road = np.array([0,1,1,0,1])
    ob = Traffic(road)
    print(ob.movement())