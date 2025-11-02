# pole = [navratova_cast for premenne in zoskupenie if podmienka]

# pre if cast nepouzivam else

# Priklad: chceme pre parne cisla od 0 do 20 vypisat ich nasobky 10
# Varianta klasicky for
numbers = range(0,20)
result = []
for number in numbers:
    if number % 2 == 0: #modulo ktorz vracia zvysok po deleni
        result.append(number*10)
print(result)
# Varianta list comprehension
result=[number*10 for number in range(0,20) if number %2 == 0]
print(result)
# Varianta list comprehension s else
result=[number*10 if number %2 == 0 else number*30 for number in range(0,20) ]
print(result)

# Priklad: mame string pre ktorz chceme urobit pole,v ktrom bude pre kazde slovo stringu cislo vyjadrujuce pocet pismen
string = "Ucim sa Python cez youtube s Misom"
print(string.split()) #funkcia na rozdelenie stringu na slova
#Varianta s for cyklom
result = []
for slovo in string.split():
    result.append(len(slovo))
print(result)
# Varianta list comprehension
result = [len(slovo) for slovo in string.split()]
print(result)

# Priklad - domaca uloha:
# Napis funkciu list_of_lists ktora dostane na vstupe cez parameter pole celych cisel vacsich ako 0 napr. [0,2,3,2]
# Nasledne vrati pole cisel ktore bude obsahovat pre kazde cislo pole s cislami od 0 po to dane cislo

# pre vstup [0,2,3,2]
# vrati [[0], [0,1,2], [0,1,2,3], [0,1,2]]
# Musti to btr funkcia !! 

#skuska
import random
p =6
pole1 =[random.randint(0,p) for item in range(0,p)]
pole2 =[list(range(0,r+1)) for r in pole1]
print(pole1)
print(pole2)

#funkcia
def list_of_lists(n):
    pole1 =[random.randint(0,p) for item in range(0,p)]
    pole2 =[list(range(0,r+1)) for r in pole1]
    print(pole1)
    print(pole2)

list_of_lists(6)
