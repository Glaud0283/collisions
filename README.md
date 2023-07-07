# About The Project

### Goal
###### Collisions are important in physic based programming (e.g in mechanics, numerical methods, game development). This library allows users to calculate final velocities of 2 particles after the collision in 3D space by 
taking into consideration of coefficient of restitution.


# Structure
###### This program starts with a definition of a class, `particle`. This class defines a particle in 3D space with a mass and space value in 3 axis.
###### First function, `restitution_coef()` calculates coefficient of restitution if it is not given in the problem.
###### Main function, `collide()` calculates the final velocities of the particles by using impulse-momentum relations in mechanics. The equations used are formed by using conservation of momentum and energy relations.


# Future
###### To develop the project, there are some advanced problem solution methods in my mind:
###### Improving `collide()` algorithm for solutions of porblems that contains collision of multiple particles.
###### Include new functions for solution of other mechanic problems, such as explosion and implosion, harmonic motion and frictional problems
