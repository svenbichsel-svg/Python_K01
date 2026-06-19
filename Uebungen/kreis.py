import math
R = float(input("Bitte gib den Radius des Kreises ein: "))

D = 2 * R
U = 2 * math.pi * R
A = R**2 * math.pi


print("Radius:      ", R)
print("Durchmesser: ", D)
print("Umfang:      ", U)
print("Flaeche:     ", A)