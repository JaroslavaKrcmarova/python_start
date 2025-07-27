# FOR FACTORIAL
def funckia_faktorial1(cislo):
    faktorial = cislo
    for i in range(1,cislo):
        faktorial = faktorial * (cislo-i)
    print(faktorial)

funckia_faktorial1(6)

# WHILE FACTORIAL 
def funckia_faktorial2(cislo):
    faktorial = 1
    faktorial_part = 1
    while faktorial_part <= cislo:
        faktorial = faktorial * faktorial_part
        faktorial_part += 1
    print(faktorial)

funckia_faktorial2(6)

# RECURSIA FACTORIAL 
def funckia_faktorial3(cislo):
    if cislo == 0:
        return 1
    return cislo * funckia_faktorial3(cislo-1)

print(funckia_faktorial3(6))

#pre kazdy prvok pola vrati pole faktorialov tzchto cisel

def reduce_multiple(a,b):
    return a*b

numbers = [1,2,3,4]
print(list(map(lambda z :reduce(lambda x,y: x*y, (range(1,z+1))),numbers)))
