import numpy as np 
import matplotlib.pyplot as plt
class Orbital_Motion(object):
    def __init__(self, steps, length, mass_mars, mass_phobos, radius_mars, radius_phobos):
        self.steps = steps # number of timesteps
        self.length = length # length of each timestep 
        self.mass_mars = mass_mars
        self.mass_phobos = mass_phobos
        self.radius_mars = radius_mars
        self.radius_phobos = radius_phobos
        self.G = 6.67*(10)**(-11)
        self.seperation = radius_mars - radius_phobos
    def mars_phobos_force(self,time):
        F = self.G*(self.mass_phobos*self.mass_mars)/(self.radius_integration(time))**2

        #  to be completed
    def velocity_integration(self,time):
        v_inital = ((self.G * self.mass_mars)/self.seperation)**0.5
        t = 0
        v = v_inital
        V = [v_inital]
        for i in range(self.steps):
            t = t + self.length
            v = v + self.accel_integration(t) * self.length
            V.append(v)
    def accel_integration(self,time):
        return 12111

    def radius_integration(self,time):
        r_initial = self.seperation
        t = 0
        r = r_initial
        R = [r_initial]
        for i in range(self.steps):
            t = t + self.length
            r = r + self.velocity_integration(t)*self.length
            R.append(r)