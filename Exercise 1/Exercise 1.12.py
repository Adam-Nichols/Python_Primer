from numpy import log
from math import pi

#Units used are cm, g, C, sec
egg_mass = 67
egg_denisty = 1.038
egg_shc = 3.7
egg_thermal_conductivity = 5.4*10**-3

water_temp = 100
centre_temp = 70
egg_origin = input("Please type \"fridge\" if the egg has been taken from the fridge or \"room\" otherwise: ")

if egg_origin == "fridge":
    egg_start_temp = 4
else:
    egg_start_temp = 20

cook_time = ((egg_mass**(2/3)*egg_shc*egg_denisty*(1/3))/(egg_thermal_conductivity*pi**2*(4*pi/3)**(2/3)))*log(0.76*((egg_start_temp-water_temp)/(centre_temp-water_temp)))

print("The time to cook the perfect egg is {} seconds!".format(int(round(cook_time,0))))
