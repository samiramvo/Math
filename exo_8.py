import math

print("Calculer l'aire d'un secteur:")
rayon=float(input("Entrez le rayon d'un cercle:"))
mes=float(input("Entrez la mesure de l'angle:"))
print("Zone secteur:",(math.radians(mes)*(rayon**2)/2))