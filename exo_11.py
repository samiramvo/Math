def difference(n=2):
    a=b=0
    for num in range(1,n+1):
        a+=num**2
        b+=num
    b=b**2
    return b-a

print(difference(12))