import numpy as np 
import matplotlib.pyplot as plt
class Orbital_Motion(object):
    def __init__(self, time_step, length, mass_mars, mass_phobos, radius_mars, radius_phobos):
        self.step = time_step
        self.length = length
        self.mass_mars = mass_mars
        self.mass_phobos = mass_phobos
        self.radius_mars = radius_mars
        self.radius_phobos = radius_phobos
    