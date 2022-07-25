
from itertools import count
print("La somme de tout les diviseurs propres:")
def get_factors(n):
    liste=[]
    for i in range(1,n+1):
        if n%i==0:
            liste.append(i)
    return liste.count()

print(get_factors(8))