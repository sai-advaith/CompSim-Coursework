import numpy as np 
import matplotlib.pyplot as plt 
class Traffic(object):
    def __init__(self,road):
        self.road = road
    def movement(self):
        k = len(self.road)
        for i in range(k):
            if (self.road[i] == 1):
                if (i < k -1 and self.road[i+1] == 0):
                    self.road[i+1] = 1
                    self.road[i] = 0
                elif ( i == (k - 1) and self.road[0] == 0):
                    self.road[0] = 1
                    self.road[i] = 0
            elif (self.road[i] == 0 and i < k - 1):
                if (self.road[i] == 0):
                    if(i == 0 and self.road[k-1] == 1):
                        self.road[i] = 1
                        self.road[k-1] = 0
                    elif(i > 0 and self.road[i-1] == 1):
                        self.road[i] = 1
                        self.road[i-1] = 0
            
        return self.road

