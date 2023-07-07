class Particle:
    def __init__(self, m, vx, vy, vz):
        self.mass = m
        self.vx = vx
        self.vy = vy
        self.vz = vz

def restitution_coef(v1, v2, u1, u2):
    """
    Calculates the coefficient of restitution.
    coefficient of restitution, e, is a value between 0 and 1.
    e = 1 represents a perfectly elastic collision and e = 0 represents a perfectly inelastic collision.
    
    Args:
        v1 (float): Initial velocity of particle 1
        v2 (float): Initial velocity of particle 2
        u1 (float): Final velocity of particle 1
        u2 (float): Final velocity of particle 2
        
    Returns:
        float: The coefficient of restitution
    """

    e = (u2 - u1) / (v1 - v1)
    return e


def collide(e, obj1, obj2):
    """
    Calculates the final velocities of two particles after a collision using the coefficient of restitution.
    coefficient of restitution, e, is a value between 0 and 1.
    e = 1 represents a perfectly elastic collision and e = 0 represents a perfectly inelastic collision.
    
    Args:
        e (float): Coefficient of restitution.
        obj1 (object): Particle 1
        obj2 (object): Particle 2
        

    Returns:
        Tuple[list, list]: Final velocity vectors of particle 1 and particle 2.
    """
    
    m1 = obj1.mass
    v1x = obj1.vx
    v1y = obj1.vy
    v1z = obj1.vz

    m2 = obj2.mass
    v2x = obj2.vx
    v2y = obj2.vy
    v2z = obj2.vz

    u1x = (m1 * v1x + m2 * v2x + m2 * e * (v2x - v1x)) / (m1 + m2)
    u2x = e * (v1x - v2x) + u1x

    u1y = (m1 * v1y + m2 * v2y + m2 * e * (v2y - v1y)) / (m1 + m2)
    u2y = e * (v1y - v2y) + u1y

    u1z = (m1 * v1z + m2 * v2z + m2 * e * (v2z - v1z)) / (m1 + m2)
    u2z = e * (v1z - v2z) + u1z

    u1 = [u1x,
          u1y,
          u1z]
    
    u2 = [u2x,
          u2y,
          u2z]
    
    return (u1, u2)
    


    



