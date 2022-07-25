def algo_babylo(number):
    if number==0:
        return number
    g=number/2
    g2=number+1
    while(g != g2):
        n=number/g
        g2=g
        g=(g+n)/2
    return g

print(algo_babylo(16))
