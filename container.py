from random import random, randint
from math import sin, cos, pi
import particle as prt
import json as js


class Container:
    """
    A class to represent a container for simulating particle dynamics.

    Attributes:
        num_particles (int): The number of particles in the container.
        quantum (float): The time quantum for each simulation step.
        temp (float): The temperature of the container.
        proportionality_factor (float): The proportionality factor for particle velocities.
        bounds (list): The bounds of the container in the form [width, height].
    """
    __isinit = False
    __partlist = []
    def __init__(self, num_particles, quantum, temp, proportionality_factor, bounds):
        """
        Initializes a container object with given parameters.

        Args:
            num_particles (int): The number of particles in the container.
            quantum (float): The time quantum for each simulation step.
            temp (float): The temperature of the container.
            proportionality_factor (float): The proportionality factor for particle velocities.
            bounds (list): The bounds of the container in the form [width, height].
        """
        self.proportionality_factor = proportionality_factor
        self.bounds = bounds
        self.num_particles = num_particles
        self.quantum = quantum
        self.temp = temp

    def init(self):
        """
        Initializes particle positions and velocities within the container.
        """
        velocity = self.proportionality_factor * self.temp ** 0.5
        for i in range(self.num_particles):
            vx = velocity * sin(2 * pi * random())
            vy = velocity * cos(2 * pi * random())
            x = randint(1, self.bounds[0])
            y = randint(1, self.bounds[1])
            self.__partlist.append(prt.Particle(1, x, y, vx, vy, 1))
        self.__isinit = True

    def start_simulation(self, time):
        """
        Starts the simulation of particle dynamics within the container.

        Args:
            time (float): The total time for simulation.

        Returns:
            dict: A dictionary containing particle positions at each time step.
        """
        points = {i: [] for i in range(self.num_particles)}
        t = 0
        while t < time:
            for i in range(self.num_particles):
                self.__partlist[i].execute_move(self.quantum)
                x = self.__partlist[i].px
                y = self.__partlist[i].py
                if x < 0.5:
                    self.__partlist[i].wall_collide(2)
                if y < 0.5:
                    self.__partlist[i].wall_collide(3)
                if x > self.bounds[0] - 0.5:
                    self.__partlist[i].wall_collide(4)
                if y > self.bounds[1] - 0.5:
                    self.__partlist[i].wall_collide(1)
                points[i].append((int(x), int(y)))
            for i in range(self.num_particles):
                for j in range(i + 1, self.num_particles):
                    if self.__partlist[i].is_colliding(self.__partlist[j]):
                        self.__partlist[i].execute_collision(self.__partlist[j])
            t += self.quantum
        return points

# Create a Container object
c = Container(500, 2, 100, 2, [300, 300])
c.init()

# Start simulation and get particle positions
d = c.start_simulation(1500)

# Convert particle positions to JSON format
fcont = js.dumps(d, indent=1)

# Write JSON data to file
file = open("TEST.json", 'wt')
file.write(fcont)
file.close()
