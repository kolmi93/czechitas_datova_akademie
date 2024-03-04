ODDELOVAC = 80*'-'
# 1. průměr bez použití sum
#vypočítejte průměr seznamu čísel, bez použití funkce sum nebo modulu statistics
list_cisel = [7, 14, 2, 18, 9, 12, 6, 11, 4, 16]
soucet = 0
for cislo in list_cisel:
    # chceme přičítat
    soucet += cislo
pocet = len(list_cisel)
print(f'prumer je: {soucet / pocet}')

print(ODDELOVAC)
# 2. vytvoř nový slovník pro chladné a teplé měsíce, kdy jsou děleny 20 stupni Celsia
rocni_teploty = {
    "Leden": 5.0,
    "Únor": 6.5,
    "Březen": 10.2,
    "Duben": 15.8,
    "Květen": 20.7,
    "Červen": 25.4,
    "Červenec": 28.3,
    "Srpen": 27.8,
    "Září": 24.2,
    "Říjen": 18.3,
    "Listopad": 12.1,
    "Prosinec": 7.0
}

teple_mesice = {}
for key, value in rocni_teploty.items():
    if value > 20:
        teple_mesice[key] = value
print(teple_mesice)

chladne_mesice = {}
for key, value in rocni_teploty.items():
    if value < 20:
        chladne_mesice[key] = value
print(chladne_mesice)

print(ODDELOVAC)

# zeptej se uživatele na jméno a zapiš do souboru tisíckrát. (.txt) "Já, {jméno} budu po digitální akademii pravidelně procvičovat python."
name = input("Jaké je Vaše jméno?\n")
veta = f'Já, {name} budu po digitální akademii pravidelně procvičovat python.\n'

with open("veta.txt", "w", encoding= 'utf-8') as soubor:
    for _ in range (1000): # místo 'i' profící použijou '_' (zahazovací proměná)
        soubor.write(veta)

veta_2 = f'Já, {name} budu po digitální akademii pravidelně procvičovat python.'
with open("veta_2.txt", "w", encoding= 'utf-8') as soubor:
    for _ in range (1000): # místo 'i' profící použijou '_' (zahazovací proměná)
        soubor.write(veta + '\n')

print(ODDELOVAC)

# odstraň duplicity z listum které budou obsahovat unikátní záznamy
pocatecni_cisla = [1,2,2,3,4,4,5]
unikatni_list = []
for cislo in pocatecni_cisla:
    if cislo not in unikatni_list:
        unikatni_list.append(cislo)
print(unikatni_list)

print(ODDELOVAC)

# pokud budu spojovat a procházet více seznamů:
pocatecni_cisla = [1,2,2,3,4,4,5]
pocatecni_cisla_2 = [1,2,2,3,4,4,5]
pocatecni_cisla_3 = [1,2,2,3,4,4,5]
vsechny = pocatecni_cisla+pocatecni_cisla_2+pocatecni_cisla_3
duplicity = []
unikatni_list = []
for cislo in vsechny:
    if cislo not in unikatni_list:
        unikatni_list.append(cislo)
    else:
        duplicity.append(cislo)
print(unikatni_list)
print(duplicity)

print(ODDELOVAC)

# Spoj 2 listy do nového jednoho listu, kdy se budou z jednotlivých listů vkládat na přeskáčku
složený_list = []
list_1 = ['P', 't', 'o', ' ', 'e', 'n', 'j', 'e', 'š', ' ', 'r', 'g', 'a', 'o', 'a', 'í', 'j', 'z', 'k', 'n', ' ', 'v', 't', '!']
list_2 = ['y', 'h', 'n', 'j', ' ', 'e', 'l', 'p', 'í', 'p', 'o', 'r', 'm', 'v', 'c', ' ', 'a', 'y', ' ', 'a', 's', 'ě', 'ě', ' ']

for item1, item2 in zip(list_1, list_2):
  složený_list.append(item1)
  složený_list.append(item2)
print(složený_list)

veta_3 = ''.join(složený_list)
print(veta_3)

print(ODDELOVAC)

#seznam jmen roztřiď do slovníku
names = ["Alice", "Bob", "Eve", "Charlie", "Amy", "Daniel", "Bella"]

from collections import defaultdict

names_dict = defaultdict(list) #za defaultdict dát do závorky název funce, která vytvoří tu konstrukci, co chceme
for name in names:
  names_dict[name[0]].append(name)

# Výpis slovníku
print(names_dict)

# Jak v Pythonu uložíš do proměnné z prvních n znaků z proměnné z? A jak posledních m znaků?
z = "ahoj světe"
první_5 = ""
for i in range(5):
  první_5 += z[i]

posledni_5 = ""
for i in range(len(z) - 5, len(z)):
  posledni_5 += z[i]

print(první_5)
print(posledni_5)

# Prochází čísla v rozsahu 0-100, kdy vypisuje čísla, která jsou dělitelná 3 a zároveň mají zbytek 2.
for i in range(0, 100):
    if i % 3 == 2:
        print(i)

# Enumerate vezme nějaký seznam, v našem případě 'l'. Ke každému prvku v listu přiřadí číslo. A část x%2==0 atd. nám vypíše všechny prvky v listu, které mají přířazenou hodnotu dělitelnou bezezbytku 2. Čísluje od 0. Tzn. vyprintuje Adam, Jaromír, Zuzana. Protože ty mají přiřazenou hodnotu: 0,2,4
l = ["Adam", "Ondra", "Jaromír", "Jágr", "Zuzana", "Hejnová"]

for x, y in enumerate(l):
    if x % 2 == 0:
        print(y)
        print(x)

# Dělá to samé, co jsem uváděla u předchozího kódu s tím rozdílem, že vypsané jméno bude mít takovou hodnotu, která má po vydělení 2 zbytek 1. Tzn. vyprintuje se: Ondra, Jágr, Hejnová s přiřazenými hodnotami: 1,3,5
l = ["Adam", "Ondra", "Jaromír", "Jágr", "Zuzana", "Hejnová"]
for x, y in enumerate(l):
    if x % 2 == 1:
        print(y)
        print(x)

# To hodí chybu "not all arguments converted during string formatting". To je tím, že my chceme dělit číslo 2 beze zbytku, ale uplatňujeme to na stringovou hodnotu (y). Aby to fungovalo, musel by být kod napsán id x%2==0: print(x)
#for x, y in enumerate(l):
#   if y % 2 == 0:
#        print(x)

# Fibonacciho posloupnost je nekonečná posloupnost čísel, ve které je každé číslo součtem dvou předchozích. Začátkem této posloupnosti jsou čísla: 0, 1, 1, 2, 3, 5, 8, 13 atd. Napiš funkci fib(x), která vrátí prvních x prvků této posloupnosti v podobě seznamu. Můžeš napsat kód v Pythonu nebo alespoň myšlenkový postup v češtině (ale aspoň strukturovaný po řádcích, aby bylo zřejmé, že víš, jakým způsobem bys postupovala).
# 👉 Tip: Pokud nevíš, jak na prvních x, můžeš napsat nekonečný cyklus. Začni s prvky 0 a 1, všechny ostatní už si potom můžeš vygenerovat výše uvedeným způsobem.
def fibonacci(choice):
    fib = [0, 1]
    while len(fib) < choice:
        sum = fib[-1] + fib[-2]
        fib.append(sum)
    return fib

choice = int(input('Zvolte si počet prvku Fibonacciho posloupnosti, který chcete zobrazit.\n'))
fib = fibonacci(choice)
print(fib)

# Jak v Pythonu uložíš třetí znak z proměnné x do proměnné y?

# 3a
a = "soustruh"
print(a)

# 3b 
b = a[2]
print(b)

# 3c
# posledních 5
c = a[-5:]
print(c)
# prvních 5
d = a[:5]
print(d)


#7. koláč za milion
#Zeptej se uživatele na celé kladné číslo (kromě nuly).
#Poté ve smyčce (while) kontroluj:
#- dokud číslo není "1"
#  - pokud je sudé, vyděl ho 2
#  - jinak ho vynásob třemi a přidej jedničku
#Jakou dostaneš sérii císel?
#Skončíme pokaždé u jedničky, nebo pro nějaká čísla série nikdy nekončí?

def kolac_milion(question):
  cisla = []
  while question > 1:
    if question % 2 == 0:
      pie = question // 2
      cisla.append(pie)
    else:
      pie = (question * 3) + 1
      cisla.append(pie)
    question = pie
  return cisla

question = int(input('Zvojte si libovolné celé kladné číslo (kromě nuly):\n'))
cisla = kolac_milion(question)
print(cisla)

# Ahoj Kubo, posílám svoje řešení koláče. Vyšlo mi, že série vždycky skončí na 1. Zkoušela jsem to několikrát spustit. Vždycky, ať už bylo zadané číslo liché či vzniklo při dělení (v podmínce IF), tak to tím *3+1 zvětšilo na sudé číslo, které se pak dalo dělit 2. A jede to do té doby, než skončí na 