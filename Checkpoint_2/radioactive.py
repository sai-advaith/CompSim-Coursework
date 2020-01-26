import random
class Radioactive(object):
    def  __init__(self,const,matrix,timestep):
        self.const = const 
        self.matrix = matrix
        self.timestep = timestep
        self.prob = const*timestep
    def half_check(self):
        """
        Boolean function to see if half of the nuclei decayed
        """
        k  = len(self.matrix) * len(self.matrix)
        return self.decayed() >= k / 2 # function to detect if half_life has been attained
    def __str__(self):
        """
        String representation of the 2d array
        """
        s = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                s = s + str(self.matrix[i][j]) + " "
            s = s + "\n" # printing the nuclei of the element as a string
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
                            self.matrix[i][j] = 1 # random.random() giving the ranom number between 0 and 1 as probability is never greated than one or less than 0
            half_life += self.timestep # adding timestep after every N nuclei iterated
        return half_life           
    def decayed(self):
        """
        In this method we will be showing the number of decayed atoms
        """
        c = 0 # counting the decayed nuclei
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                if self.matrix[i][j] == 1:
                    c += 1 # counting the number of decayed nuclei
        return c