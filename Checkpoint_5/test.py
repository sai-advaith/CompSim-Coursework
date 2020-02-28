from space import Space
if __name__ == "__main__":
	iterations = int(input("number of iterations: "))
	length = float(input("length of each time step: "))
	mass_mars = 6.4185e+23
	mass_phobos = 1.06e+16
	orbit_phobos = 9.3773e+6
	motion = Space(iterations,length,mass_mars,mass_phobos,orbit_phobos)