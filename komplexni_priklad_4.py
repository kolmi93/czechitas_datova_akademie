import pandas as pd

# nacteni do dataframu data
data = pd.read_csv('battles.tsv', sep='\t')

# vytvarim si serii (dlouhy seznam) z dataframe
# tak, že spojim ctyri sloupce dohromady
serie_utocniku = pd.concat(
    [
        data['attacker_1'],
        data['attacker_2'],
        data['attacker_3'],
        data['attacker_4'],
    ]
)

# vytvorim vysledek napocitanim serie utocniku
vysledek = serie_utocniku.value_counts()
print(vysledek)
# alternativni zpusob použití value_counts primo z pandas modulu
# vysledek2 = pd.value_counts(serie_utocniku)

vysledek.to_csv('utocnici_4.csv', header=False)