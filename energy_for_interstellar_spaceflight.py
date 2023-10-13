import math
import astropy.units as u
import astropy.constants as c

def v(x, P, m):
    """Returns lowest-energy velocity given distance to destination, power, and mass.
    x: distance to destination
    P: power required for voyage
    m: mass"""
    return ((P*x)/m) ** (1/3)

def E(x, P, m):
    """Returns lowest energy given distance to destination, power, and mass. The parameters are the same as for v."""
    vel = v(x, P, m)
    return (m*vel*vel) / 2 + (P*x)/vel

print("This is a classical interstellar voyage calculator. It will give values for a minimum energy.")
print("Please note that Special Relativity will give more pessimistic values.")
x = float(input("Distance in light years: ")) * u.lyr
P = float(input("Power requirement in Watts: ")) * u.W
m = float(input("Mass requirement in kg: ")) * u.kg
vel = v(x, P, m).to("lyr / yr")
nrg = E(x, P, m).to("TJ")
# Relativity: sqrt(1-0.1^2) = 0.99498743710662. Classical case assumes it's 1; <1% error
if vel / c.c > 0.1:
    print("Warning: velocity > 0.1c. Special Relativity will be a significant issue with these numbers.")
print("Velocity:", vel)
print("Energy:", nrg)
print("Time to Destination:", (x/vel).to("yr"))
