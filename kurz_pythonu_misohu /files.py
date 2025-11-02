# Citanie suboru
with open("C:/Users/Root/Documents/Python/kurz_pythonu_misohu_moje_poznamky/subor_test.txt","r") as file:
    data = file.readlines()
print(data)
print(list(reversed(data)))

with open("C:/Users/Root/Documents/Python/kurz_pythonu_misohu_moje_poznamky/subor_test.txt","r") as file:
    for line in file.readlines():
        print(line, end='')

# Zapis do suboru / zapis noveho suboru
with open("subor_novy.txt","w") as file:
    for word in ["Zapisujem","novy","subor"]:
        file.write(word)
        file.write(" ") # po kazdom slove medzera

# Pridanie do existujuceho suboru
with open("subor_novy.txt","a") as file:
    for number in [1,2]:
        file.write(str(number))
        file.write(",")
