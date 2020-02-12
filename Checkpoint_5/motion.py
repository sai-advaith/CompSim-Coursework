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
    def mars_phobos(self):
        distance = abs(self.radius_mars - self.radius_phobos)
        F = self.G*(self.mass_phobos*self.mass_mars)*distance
        #  to be completed
    def velocity_integration(self,time):
        v_inital = ((self.G * self.mass_mars)/self.seperation)**0.5
        t = 0
        for i in range(self.steps):
            t = t + self.length
            