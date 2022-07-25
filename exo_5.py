import math

print("Calcul aire et surface du cylindre:")
base=float(input("Entrez la base:"))
hauteur=float(input("Entrez la hauteur:"))
rayon=float(input("Entrez le rayon:"))
print("Volume:",(base*hauteur))
print("Surface:",(math.pi*(rayon**2)))