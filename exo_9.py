print("Calcul du discriminant:")

x=float(input("Valeur de x:"))
y=float(input("Valeur de y:"))
z=float(input("Valeur de Z:"))

def discriminant(x,y,z):
    dis=(y**2)-(4*x*z)
    if dis>0:
        print("Two solutions",dis)
    if dis<0:
        print("One solution",dis)
    if dis==0:
        print("Pas de solution réelles")

discriminant(x,y,z)