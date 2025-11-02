
""" 
Dictionary = {
    "key1" = "value1",
    "key2" = "value2",
}
"""
# PRVY SLOVNIK
my_dict= {
    "Jarka" : 34,
    "Jozef" : 36,
    True: "True",
    False: True,
}
print(my_dict)
print(type(my_dict))

# Pristup k prvkom - hranate zatvorky
print(my_dict['Jarka'])

# Priradenie novej hodnoty klucu
my_dict['Jarka'] = 35
print(my_dict['Jarka'])

# Zmazanie prvku del  
del my_dict['Jarka'] #del je jeden zo sposobou mazania
print(my_dict)

# DRUHY SLOVNIK s vnorenym slovnikom
osoba = { 
    "meno" : "Jaroslava", 
    "priezvisko": "Krčmárová", 
    "jazyk": ["slovenčina", "čeština", "angličtina"],
    "adresa": {
        "mesto": "Florida",
        "ulica": "Pobrežná",
        "číslo": 6
    }
}

#
# GET() pristupenie k prvku / vnorenemu
print(osoba["adresa"]["mesto"])
print(osoba.get("adresa"))  #Funkcia GET
print(osoba.get("adres","Prvok neexistuje"))  #Funkcia GET s druhzm prvkom - ten sa vzpise pokial prvok neexistuje

#
# ITEMS() vytvorenie pola klucov a hodnot list(osoba.items())
for kluc,hodnota in list(osoba.items()):
    print("Kluc je ",kluc)
    print("Hodnota je",hodnota)

for kluc,hodnota in list(osoba.items()):
    print("Kluc je ",kluc)
    if type(hodnota) == dict :
        for kluc1,hodnota1 in hodnota.items():
            print("Podkluc je ",kluc1)
            print("Hodnota je ",hodnota1)
    else:
        print("Hodnota je",hodnota)

#
# KEYS() vracia list klucov
print(osoba.keys())

#
# VALUES() vracia list hodnot
print(osoba.values())

#
# POP("kluc") vrati hodnotu definovanu na kluci a vymaze prvok zo slovniku
print(osoba["priezvisko"])
osoba.pop("priezvisko")
print(osoba.keys())

#
# POPITEM() vrati posledny prvok slovniku a zmaze ho 
osoba.popitem()
print(osoba.keys())
