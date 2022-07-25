print("Voir si le nombrs est abondants")
liste=[]
def get_factors(n):
    for i in range(1,n+1):
        if n%i==0:
            liste.append(i)
    if sum(liste)>n:
            print("Ce nombre est abondant")
    else:
            print("Ce nombre n'est pas abondant")

get_factors(12) 