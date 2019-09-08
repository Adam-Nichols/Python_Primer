from math import  pi, sqrt

football_drag_coef = 0.2
football_mass = 0.43
football_radius = 0.11
air_density = 1.2
gravity = 9.81


football_projected_area = pi * football_radius ** 2

def drag(ball_speed):
    drag_force = 0.5 * football_drag_coef * air_density * football_projected_area * ball_speed ** 2
    return round(drag_force,2)

def grav():
    grav_force = football_mass*gravity
    return round(grav_force,2)

def terminal_velc():
    terminal_velc = sqrt((2*football_mass*gravity) / (air_density * football_projected_area * football_drag_coef))
    return round(terminal_velc)

print("The resistance due to air after a soft kick is {} N and {} N after a hard kick, the force due to gravity is {} N. The terminal velocity of the ball is {} m/s".format(drag(2.77),drag(33.33),grav(),terminal_velc()))
