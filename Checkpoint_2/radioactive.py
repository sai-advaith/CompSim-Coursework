class Radiactive(object):
    def  __init__(self,const,matrix,timestep):
        self.const = const
        self.matrix = matrix
        self.timestep = timestep
    def half_check(self):
        """
        boolean function to see if half of the nuclei decayed
        """
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
    def prob(self):
        """
        In this method we will determine the probability of decay
        """
