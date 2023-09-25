# ÚKOL Č. 1: 
pohyby = [1200, -250, -800, 540, 721, -613, -222]

# Vypište v pořadí třetí pohyb z uvedeného seznamu.
treti = pohyby[2]
print(treti)

# Vypište všechny pohyby kromě prvních dvou.
krome_1_2 = pohyby[2:]
print(krome_1_2)

# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))

# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(min(pohyby))
print(max(pohyby))

# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))

# ÚKOL Č. 2: Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.
s = [352, 154, 823, 335, 999, 124, 536]
t = [352, 154, 823, 335, 999]
u = [352, 154]

prum_1 = round(sum(s)/len(s))
print(prum_1)
prum_2 = round(sum(t)/len(t))
print(prum_2)
prum_3 = round(sum(u)/len(u))
print(prum_3)

# ÚKOL Č. 3: Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.
rozpeti = max(s)-min(s)
print(rozpeti)
rozpeti_2 = max(t)-min(t)
print(rozpeti_2)
rozpeti_3 = max(u)-min(u)
print(rozpeti_3)

# ÚKOL Č. 4: Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.
import math
uprostred_s = math.floor(len(s) // 2)
uprostred_t = math.floor(len(t) // 2)
uprostred_u = math.floor(len(u) // 2)
print(s[uprostred_s])
print(t[uprostred_t])
print(u[uprostred_u])

# ÚKOL Č. 5: Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k začátku seznamu.
import math
uprostred_s2 = math.floor((len(s) -1) // 2)
uprostred_t2 = math.floor((len(t) -1) // 2)
uprostred_u2 = math.floor((len(u) -1) // 2)
print(s[uprostred_s2])
print(t[uprostred_t2])
print(u[uprostred_u2])

# ÚKOL č. 6: Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena
#jmeno = input("Napiště své jméno:\n")
#print(jmeno.lower())
#print(jmeno.upper())

# ÚKOL č. 7: Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:
hodnoty = ['12', '1', '7', '-11']
nova_hodnota = (int(hodnoty[2])+4)
hodnoty.remove('7')
hodnoty.insert(2, nova_hodnota)
print(hodnoty)

# ÚKOL Č. 8: Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla zadána nikoliv v seznamu, ale v řetězci oddělená mezerou. K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal takto
hodnoty_2 = '12.1 1.68 7.45 -11.51'
vysledek = hodnoty_2.split(" ")
print(vysledek)
uprava = (float(vysledek[3]) + 0.25)
print(uprava)
vysledek.remove('-11.51')
vysledek.insert(3, uprava)
# vysledek.append(uprava)
print(vysledek)

# ÚKOL Č. 9: Zkuste vymyslet, jak udělat zápis příkazů ze cvičení Čísla jako text co nejúspornější. Dá se dojít až k tomu, že celé řešení bude na jeden řádek.

# ÚKOL Č. 10: Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.
import math
number = float(input("Napiště libovolné desetinné číslo:\n"))
# nahoru
nahoru = math.ceil(number)
print(nahoru)
# dolu
dolu = math.floor(number)
print(dolu)
# klasicky pythonovsky
pythonovsky = round(number)
print(pythonovsky)

# ÚKOL Č. 11: Uvažuj, že student se hlásí na školu, která vybírá studenty podle průměru. Pro školu jsou ale důležité pouze předměty český jazyk, anglický jazyk, matematika a fyzika. Vypočítej průměr studenta z daných předmětů s využitím modulu statstics. Na začátku vytvoř prázdný seznam a následně pomocí cyklu vlož do nového seznamu známky ze čtyř vyjmenovaných předmětů. Nakonec použij metodu statistics.mean() k výpočtu průměru. Dále zkus využít funkce, které jsou zmíněné v textu, k výpočtu nejlepší a nejhorší známky z daných předmětů.
import statistics
school_report = [
    ["Český jazyk", 1],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
# Vytvoř prázdný seznam pro známky ze čtyř předmětů
important_subjects = []

# Vložení 4 předmětů do nového seznamu
for subject in school_report:
    if subject[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
        important_subjects.append(subject[1])

# Vypočítej průměr známek ze čtyř předmětů
average = statistics.mean(important_subjects)

# Vypočítej nejlepší a nejhorší známku ze čtyř předmětů
best_grade = max(important_subjects)
worst_grade = min(important_subjects)

print(f"Průměrná známka z vybraných předmětů u žáka XY je: {average}). Nejlepší známka je: {best_grade} a nejhorší {worst_grade}.")

# Ve statistice existuje ukazatel zvaný modus, který vrátí nejčastější hodnotu v datech. V modulu statistics existuje funkce mode(), která umí modus spočítat. Funkce mode() má navíc vychytávku, umí pracovat i s řetězci.

# ÚKOL Č. 12: Uvažuj data v seznamu votes, což je hlasování zaměstnanců malé firmy o tom, jakou akci podniknou během jejich vánočního večírku. Použij funkce mode() ke zjištění, pro jakou aktivitu hlasovalo nejvíce zaměstnanců. Funkce má jeden parametr - seznam, ze kterého má určit nejčastější prvek.
votes = [
    "curling", 
    "vánoční svařák na trzích", 
    "vánoční svařák na trzích", 
    "curling", 
    "zážitková první pomoc",
    "curling", 
    "zážitková první pomoc",
    "curling",
    "zážitková první pomoc",
    ]

import statistics
print(statistics.mode(votes))

# ÚKOL Č. 13: Následující tabulka obsahuje průměrné roční teploty v České republice za roky 2001 až 2010 (zdroj: Český hydrometeorologický ústav).
zip()
roky = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
teploty = [7.8, 8.7, 8.2, 7.8, 7.7, 8.2, 9.1, 8.9, 8.4, 7.2]

# vytvoření vnořeného seznamu pomocí funkce zip
radky = []
for rok, teplota in zip (roky, teploty):
    radky.append([rok, teplota])
print(radky)
# vytvoření pomocí seznamu sloupců
sloupce = [roky, teploty]
print(sloupce)

# Získejte teplotu na třetím řádku tabulky.
teplota_1 = radky[2][1]
print(teplota_1)

teplota_2 = sloupce[1][2]
print(teplota_2)

# Získejte rok na pátém řádku tabulky.
rok_1 = radky[4][0]
print(rok_1)

rok_2 = sloupce[0][4]
print(rok_2)

# Získejte poslední řádek tabulky jako seznam.
last_1 = radky[-1]
print(last_1)

last_2 = []
last_2.append(sloupce[0][-1])
last_2.append(sloupce[1][-1])
print(last_2)

# Vytvořte tabulku bez prvních dvou řádků.
select_1 = []
select_1.append(radky)
select_1.remove[0]

select_2 = []
select_2.append(sloupce)

# Vytvořte tabulku pouze z prvních dvou řádků.
# Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
# Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.