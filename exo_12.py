def power_base(base,power):
    return sum([int(i)for i in str(pow(base,power))])

print(power_base(2,100))