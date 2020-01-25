import numpy as np
from radioactive import Radiactive
if __name__ == "__main__":
    """
    Main method
    """
    N = int(input("number of the Iodine-128: "))
    decay_constant = float(input("decay constant: "))
    t_step = float(input("timestep: "))
    matrix = [[0 for _  in  range(N)] for _ in range(N)]
    i = Radiactive(decay_constant,matrix,t_step)
    half = np.log(2) / decay_constant
    k = i.decay()
    print(str(i))
    print("Initial number of undecayed nuclei: ", N*N,"\n")
    print("Final number of undecayed nuclei: ",N*N - i.decayed(),"\n")
    print("Simulation value of half-life: ",k,"\n")
    print("Actual value of half-life: ",half,"\n")