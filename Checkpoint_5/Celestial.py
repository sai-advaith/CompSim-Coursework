import numpy as np


class Celestial(object):
    """docstring for Celestial"""
    def __init__(self, dt, masses, positions, velocities): #constructor
        self.GRAVITATIONAL_CONSTANT = 6.67408e-11
        self.dt = dt
        self.ke = []
        accelerations = np.zeros_like(positions)
        self.vectors = np.array([positions, velocities, accelerations])
        self.scalars = np.array([masses])

    def computeAcceleration(self):
        """
        Calculating the acceleration
        """
        for (index, masses) in enumerate(self.scalars[0]):
            temp_accelerations = np.empty([len(self.vectors[2]), 2])
            temp_accelerations[index] = np.array([0., 0.])
            for (i, m) in enumerate(self.scalars[0]):
                if i != index:
                    r1 = self.vectors[0][index]
                    r2 = self.vectors[0][i]
                    temp_accelerations[i] = self.GRAVITATIONAL_CONSTANT * m / ((np.linalg.norm(r2 - r1))**2) * (1 / (np.linalg.norm(r2 - r1))) * (r2 - r1)
            self.vectors[2][index] = np.sum(temp_accelerations, axis=0)

    def computeVelocity(self):
        """
        Computing Velocity
        """
        self.vectors[1] = self.vectors[1] + (self.dt * self.vectors[2])

    def computePosition(self):
        """
        Computing Position
        """
        self.vectors[0] = self.vectors[0] + (self.dt * self.vectors[1])

    def computeKE(self):
        """
        Computing Kinetic Energy
        """
        ke = 0.5 * self.scalars[0] * (np.linalg.norm(self.vectors[1], axis=1))**2
        self.ke.append(np.sum(ke))