from collections import Counter
import pandas as pd

# načtení všech řádek do listu
with open ('battles.tsv', encoding='utf-8') as file:
    radky = file.readlines()
#print(radky)

hlavicka = radky[0]
for nazev_sloupce in hlavicka.split('\t'):
    print(nazev_sloupce)

# uložíme si pozici útočníků v tabulce jako proměnnnou
# připravueme si indexy (zjistili jsme ze souboru)
SL_UTOCNIK_PRVNI = 5
SL_UTOCNIK_POSLEDNI = 8

# slovník, do kterého budeme ukládat výsledky, jméno rodu a výsledky
utocnici = []

# procházíme řádky, ale až od druhého (první je hlavička)
for radek in radky [1:]:
    radek = radek.split('\t') #rozdělení řádek podle tabulátoru, dostaneme list

    # procházíme řádek(list) a bereme jen hodnoty ve sloupci 5-9
    # !! POZOR !! slice potřebuje na konci +1
    for jmeno_utocnika in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        # zvětšíme hodnotu o +1
        # kdy get nám dá 0, kterou my zvětšíme o 1
        if jmeno_utocnika != '':
            utocnici.append(jmeno_utocnika)

spocitani_utocnici = Counter(utocnici)

# vypis do konzole
print(spocitani_utocnici)

with open('utocnici_2.csv', 'w', encoding='utf-8') as soubor:
    # tady si hodnotu ukládáme do dvou proměnných
    for jmeno, pocet in spocitani_utocnici.most_common(): # pokud do závorky do most_common nennapíšeme hodnotu, vpíše to všechny hodnoty seřazené, pokud se vepíše číslo, vypíše jen 1.xy dle vybraného čísla
        soubor.write(f'{jmeno},{pocet}\n')