import random
class Radiactive(object):
    def  __init__(self,const,matrix,timestep):
        self.const = const
        self.matrix = matrix
        self.timestep = timestep
        self.prob = -1*const*timestep
    def half_check(self):
        """
        boolean function to see if half of the nuclei decayed
        """
        k  = len(self.matrix) * len(self.matrix[0])
        if (self.decayed() == (k / 2)):
            return True
        else:
            return False
    def __str__(self):
        """
        String representation of the 2d array
        """
        s = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                s = s + str(self.matrix[i][j]) + " "
            s = s + "\n"
        return s
    def decay(self):
        """
        In this method we will be showing the decay of the nuclei based on the timestep. return simulated half life
        """
        half_life = 0
        while(not self.half_check()):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix)):
                    if (self.matrix[i][j] == 0 and ((abs(self.prob) >= random.uniform(0,1)))):
                        self.matrix[i][j] = 1
                half_life += self.timestep
        print(self.matrix)
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