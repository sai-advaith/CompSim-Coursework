from radioactive import Radiactive
if __name__ == "__main__":
    N = int(input("number of the Iodine-128: "))
    decay_constant = float(input("decay constant: "))
    t_step = float(input("timestep: "))
    matrix = [[0]*N]*N
    i = Radiactive(decay_constant,matrix,t_step)
    print(str(i))