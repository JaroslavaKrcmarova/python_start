# map a filter funkcie su built-in
# reduce je v baliku from functools import reduce

# map(funkcia,zoskupenie) .. vracia pozmeneny prvok na vstupe, aplikuje funkciu na zoskupenie
# filter(funkcia,zoskupenie) .. funkcia vracia True/Flase pre prvok na vstupe, filter nasledne filtruje zoskupenie iba na True prvky
# reduce(funkcia,zoskupenie) .. redukuje na mensi list
# lamba funkcia ... def: lamba x:print(x) .. zjednodusuje kod

# MAP priklad: pole čísel dáme na druhú
numbers = [2,3,4,5]
def return_power(number,power=2):
    return number**power
print(list(map(return_power,numbers)))# prve riesenie
print(list(map(lambda number : number**2,numbers)))# druhe riesenie ma iba riadok

# MAP priklad: z pola čísel vytvori pole kde bude kazdy prvok tuple obsahujuci zaporne a kladne cislo z povodnych prvkov
# tj pre [1,2,3] vztvori [(-1,1),(-2,2),(-3,3)]
numbers = [2,3,4,5]
print(list(map(lambda number : (-number,number),numbers)))

# FILTER chceme iba parne cisla
numbers = [2,3,4,5]
def is_even(number):#funkcia kt. vracia True pokial je cislo parne
    return number % 2 == 0
print(list(filter(is_even,numbers)))# prve riesenie
print(list(filter(lambda number: number % 2==0,numbers)))# druhe riesenie ma iba riadok

# FILTER priklad, na vstupe bude pole od 0 po 100 a funkcia vrati tie cisla ktore su delitelne 3 a zaroven 7

def divisible_3_7(number):
    return (number % 3 == 0 and number % 7 == 0 )
print(list(filter(divisible_3_7,list(range(0,100)))))# prve riesenie
print(list(filter(lambda number: (number % 3 == 0 and number % 7 == 0 ),list(range(0,100)))))# druhe riesenie ma iba riadok

# REDUCE
from functools import reduce
# priklad z pola chceme zistit sucet
def reduce_sum(a,b):
    return a+b
print(reduce(reduce_sum,numbers))# prve riesenie
print(reduce(lambda x,y: x+y,numbers))# druhe riesenie 1 riadok

# ZAVER priklad pre kazdy prvok pola vrati pole faktorialov tzchto cisel

def reduce_multiple(a,b):
    return a*b

numbers = [1,2,3,4]
print(list(map(lambda z :reduce(lambda x,y: x*y, (range(1,z+1))),numbers)))




       
