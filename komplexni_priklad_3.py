from collections import Counter

# nacteni souboru rovnou jako vsechny radky do listu
with open('battles.tsv', encoding='utf8') as soubor:
    radky = soubor.readlines()

# pripravujeme si indexy sloupců (zjistili jsme ze souboru)
SL_UTOCNIK_PRVNI = 5
SL_UTOCNIK_POSLEDNI = 8

# list, do kterho si dame utocniky
utocnici = []

# prochazime radky, ale az od druheho (prvni je hlavicka)
for radek in radky[1:]:
    radek = radek.split('\t')  # rozdelujeme radek podle tabulatoru, dostaneme list

    # rozsirime list utocniku o vsechny utocniky z radku
    # pozor, pridavame i prazdny retezec, ale je to rychlejsi
    # ['Lan..', '', '', '']
    utocnici = utocnici + radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]


# nechame si spocitat vyskyty v listu pomoci conteru
spocitani_utocnici = Counter(utocnici)

# odstranime vyskyt prazdnych hodnot, ktere jsme predtim umyslne zanedbali
spocitani_utocnici.pop('')

# vypis do konzole
print(spocitani_utocnici)

# vypis do souboru
with open('utocnici_3.csv', 'w', encoding='utf8') as soubor:

    # pouzijem trik k serazeni "most_common"
    # most_common dava n-nejcastejsich podle velikosti
    # pokud ale n nezedame, da nam vsechny nejcastejsi -> serazene pocty :)
    for jmeno_utocnika, pocet in spocitani_utocnici.most_common():
        soubor.write(f'{jmeno_utocnika},{pocet}\n')