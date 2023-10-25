# nacteni souboru rovnou jako vsechny radky do listu
with open('battles.tsv', encoding='utf8') as soubor:
    radky = soubor.readlines()

# pripravene indexy sloupcu
SL_VYSLEDEK = 13
SL_SILA_UTOCNICI = 17
SL_SILA_OBRANCI = 18
SL_VELITEL_UTOCNICI = 19
SL_VELITEL_OBRANCI = 20

# pripraveny prazdny seznam velitelu (budeme rozsirovat)
velitele = []

# prochazim nactene radky
for radek in radky[1:]:
    radek = radek.split('\t')  # rozdeluju na seznam bunek

    # pokud jsou sila utocniku, nebo, sila obrancu prazdne
    if radek[SL_SILA_UTOCNICI] == '' or radek[SL_SILA_OBRANCI] == '':
        # nema smysl s timto radkem pokracovat
        # jdeme na zacatek for cyklu pro dalsi radek
        continue
    
    # pokud ale vse mame, pripravime si do promennych pro lepsi citelnost
    sila_utocniku = float(radek[SL_SILA_UTOCNICI])
    sila_obrancu = float(radek[SL_SILA_OBRANCI])
    vysledek_bitvy = radek[SL_VYSLEDEK]

    # tady musím zapnout hlavu
    # koukam na to z pohledu utocniku (tak je vytvorena tabulka)
    # chci pridat do seznamu ty, co prekonali presilu
    if sila_utocniku > sila_obrancu and vysledek_bitvy == 'loss':
        uspesni_velitele = radek[SL_VELITEL_OBRANCI].split(', ')
        velitele += uspesni_velitele
    elif sila_utocniku < sila_obrancu and vysledek_bitvy == 'win':
        uspesni_velitele = radek[SL_VELITEL_UTOCNICI].split(', ')
        velitele += uspesni_velitele

print(velitele)
print(uspesni_velitele)