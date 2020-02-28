import numpy as np 
import matplotlib.pyplot as plt
class Space(object):
	def __init__(self,iterations,length,mass_mars,mass_phobos,radius_phobos):
		self.G = 6.67e-11
		self.iterations = iterations
		self.length = length
		self.mass_mars = mass_mars
		self.mass_phobos = mass_phobos
		self.radius_phobos = radius_phobos
		self.T = 0
	def v_initial(self):
		"""
		Calculating the initial velocity of phobos
		"""
		v = self.G*self.mass_mars/self.radius_phobos #  usign formula given in the documentation
		return v**(1/2)
# TODO: check if the timestep inputted is way less than the period of Phobos
	def update_vel(self):
		"""
		Method to update the velocities based on the algorithm given
		"""
		velocities = [self.v_initial()]
		for i in range(1,self.iterations):
			new_v = velocities[i-1] + self.accel()*self.length
			self.T += self.length
		return velocities 
	def accel(self):
		return 0
		#TODO : implement the acceleration function
	def radius(self):
		radii = [self.radius_phobos]
		for i in range(1,self.iterations):
			new_radius = radii[i-1] +  self.update_vel()[i]*self.length
			radii.append(new_radius)
		return radii
