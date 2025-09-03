p=int(input("Principle Amount:"))
r=int(input("Rate of interest:"))
t=int(input("Total number of months:"))
SI=(p*t*r)/100
total=p+SI
print("Simple Interest=",SI)
print("Total Amont in hand=",total)