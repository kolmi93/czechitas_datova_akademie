import csv
from collections import Counter

sledovane_sloupce = ['attacker_1', 'attacker_2', 'attacker_3', 'attacker_4']
utocnici = Counter()

with open('lessons/complex_example/battles.tsv', encoding='utf8') as soubor:
    # nacitam si jendotlive radky, ale mam z nich rovnou slovniky
    data = csv.DictReader(soubor, delimiter='\t')

    # ted muzu seznam radku, slovniku, rovnou prochazet
    for radek in data:
        for nazev_sloupce, hodnota in radek.items():
            if nazev_sloupce in sledovane_sloupce and hodnota != '':
                utocnici[hodnota] += 1

print(utocnici)
# pozn: counter má pro vás připrav