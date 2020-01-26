import numpy as np 
from radioactive import Radioactive
if __name__ == "__main__":
    k = np.arange(100)
    a = []
    sum = 0
    for i in k:
        matrix = [[0 for _  in  range(i)] for _ in range(i)]
        iodine = Radioactive(0.02775,matrix,0.01)
        r = iodine.decay()
        print("test case",i,": ",r)
        sum = sum + r
    print("average half life ",sum/len(k))