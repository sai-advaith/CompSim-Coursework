import random
class Radiactive(object):
    def  __init__(self,const,matrix,timestep):
        self.const = const
        self.matrix = matrix
        self.timestep = timestep
        self.prob = const*timestep
    def half_check(self):
        """
        boolean function to see if half of the nuclei decayed
        """
        k  = len(self.matrix) * len(self.matrix)
        return self.decayed() >= k / 2
    def __str__(self):
        """
        String representation of the 2d array
        """
        s = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                s = s + str(self.matrix[i][j]) + " "
            s = s + "\n"
        print()
        print("Representation of the array of nuclei: "+"\n")
        print("0: Unedcayed nuclei")
        print("1: Decayed nuclei"+"\n")
        return s
    def decay(self):
        """
        In this method we will be showing the decay of the nuclei based on the timestep. return simulated half life
        """
        half_life = 0
        while(not self.half_check()):
            # print(half_life)
            # print()
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if (self.matrix[i][j] == 0):
                        if (abs(self.prob) >= random.random()):
                            self.matrix[i][j] = 1
            half_life += self.timestep
        return half_life           
    def decayed(self):
        """
        In this method we will be showing the number of decayed atoms
        """
        c = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    c += 1
        return c