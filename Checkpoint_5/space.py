import numpy as np 
import matplotlib.pyplot as plt
class Space(object):
	def __init__(self,G,iterations,length,mass_mars,mass_phobos,radius_phobos):
		self.G = G
		self.iterations = iterations
		self.length = length
		self.mass_mars = mass_mars
		self.mass_phobos = mass_phobos
		self.radius_phobos = radius_phobos
	def v_initial(self):
		"""
		Calculating the initial velocity of phobos
		"""
		v = self.G*self.mass_mars/self.radius_phobos #  usign formula given in the documentation
		return v**(1/2)
# TODO: check if the timestep inputted is way less than the period of Phobos
	def update_vel(self):
		"""
		Method to updat ehte velocities based on the algorithm given
		"""
		vel = [self.v_initial()]
		