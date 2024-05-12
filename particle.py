class Particle:
    """
    A class to represent a particle in a simulation.

    Attributes:
        mass (float): The mass of the particle.
        px (float): The x-coordinate position of the particle.
        py (float): The y-coordinate position of the particle.
        vx (float): The velocity of the particle in the x-direction.
        vy (float): The velocity of the particle in the y-direction.
        collision_rad (float): The collision radius of the particle.
    """

    def __init__(self, mass, px, py, vx, vy, collision_rad):
        """
        Initializes a particle object with given parameters.

        Args:
            mass (float): The mass of the particle.
            px (float): The x-coordinate position of the particle.
            py (float): The y-coordinate position of the particle.
            vx (float): The velocity of the particle in the x-direction.
            vy (float): The velocity of the particle in the y-direction.
            collision_rad (float): The collision radius of the particle.
        """
        self.mass = mass
        self.vx = vx
        self.vy = vy
        self.px = px
        self.py = py
        self.collision_rad = collision_rad

    def is_colliding(self, p2):
        """
        Checks if the particle is colliding with another particle.

        Args:
            p2 (Particle): Another particle object.

        Returns:
            bool: True if colliding, False otherwise.
        """
        dis = (self.px - p2.px) ** 2 + (self.py - p2.py) ** 2
        return True if dis < (self.collision_rad + p2.collision_rad) ** 2 else False

    def execute_collision(self, p2):
        """
        Updates the velocities of two colliding particles based on their masses and velocities.

        Args:
            p2 (Particle): Another particle object.
        """
        m1 = self.mass
        m2 = p2.mass
        total = m1 + m2
        c1 = (m1 - m2) / total
        c2 = (m1 + m1) / total
        cvx = self.vx
        cvy = self.vy
        self.vx = c1 * self.vx + c2 * p2.vx
        self.vy = c1 * self.vy + c2 * p2.vy
        p2.vx = c2 * cvx - c1 * p2.vx
        p2.vy = c2 * cvy - c1 * p2.vy

    def execute_move(self, quantum):
        """
        Updates the position of the particle based on its velocity and a given time quantum.

        Args:
            quantum (float): The time quantum for movement.
        """
        self.px += self.vx * quantum
        self.py += self.vy * quantum

    def wall_collide(self, wall_no):
        """
        Handles collisions with walls based on the wall number provided.

        Args:
            wall_no (int): The number of the wall collided with.

            Wall Numbers:
            1: Top wall
               +--------------------+
               |         1          |
               |                    |
               |                    |
               |2                  4|
               |                    |
               |                    |
               |          3         |
               +--------------------+
            2: Right wall
            3: Bottom wall
            4: Left wall
        """
        if wall_no == 1 or wall_no == 3:
            self.vy = -1 * self.vy
        else:
            self.vx = -1 * self.vx
