import numpy as np 
from traffic import Traffic
if __name__ == "__main__":
    def check(e):
        g = True
        for ch in e:
            if ch == 0 or ch == 1:
                continue
            else:
                g = False
        return g
    buffer = []
    a = int(input("size of the array:"))
    for i in range(a):
        buffer.append(int(input("element:")))
        if (not check(buffer)):
            raise ValueError("not appropriate value")
    road = np.array(buffer)
    iterations = int(input("number of require interations:"))
    tr = Traffic(road,iterations)
    tr.update()
