import numpy as np
from radioactive import Radioactive
if __name__ == "__main__":
    """
    Main method
    """
    N = int(input("number of the Iodine-128: "))
    if (N<=0):
        raise ValueError("Negative or zero atoms is not appropriate") #exception handling for negative or zero atoms
    
    decay_constant = float(input("decay constant: "))
    if (decay_constant <= 0):
        raise ValueError("Not possible") #negative decay constants 
    
    t_step = float(input("timestep: "))
    if (t_step <= 0):
        raise ValueError("Inappropriate value of timestep") #negative timestep will result in negative half life which makes no sense 

    matrix = [[0 for _  in  range(N)] for _ in range(N)] # matrix with undecayed atoms of size N*N, 0 => Undecayed 1 => Decayed
    iodine = Radioactive(decay_constant,matrix,t_step) #creating iodine object 
    half = np.log(2) / decay_constant # half life of the element based on its decay constant
    k = iodine.decay() # this will decay the atom and store its simulated half life in a variable
    
    print(str(iodine)) # printing the visualization of the atom
    print("Initial number of undecayed nuclei: ", N*N,"\n") # number of inital undecayed nuclei
    print("Final number of undecayed nuclei: ",N*N - iodine.decayed(),"\n") # final number of undecayed nuclei 
    print("Simulation value of half-life: ",k,"\n") # printing the returned value of decay()
    print("Actual value of half-life: ",half,"\n") # previously calculatedls
