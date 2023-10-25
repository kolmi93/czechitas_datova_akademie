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
utocnici = {}

# procházíme řádky, ale až od druhého (první je hlavička)
for radek in radky [1:]:
    radek = radek.split('\t') #rozdělení řádek podle tabulátoru, dostaneme list

    # procházíme řádek(list) a bereme jen hodnoty ve sloupci 5-9
    # !! POZOR !! slice potřebuje na konci +1
    for jmeno_utocnika in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        # zvětšíme hodnotu o +1
        # kdy get nám dá 0, kterou my zvětšíme o 1
        if jmeno_utocnika != '':
            utocnici[jmeno_utocnika] = utocnici.get(jmeno_utocnika, 0) + 1
print(utocnici)

with open('utocnici.csv', 'w', encoding='utf-8') as soubor:
    # tady si hodnotu ukládáme do dvou proměnných
    for jmeno, pocet in utocnici.items():
        soubor.write(f'{jmeno},{pocet}\n')