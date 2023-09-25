s = "MH,Metal Heart Radio,2022-01-14 18:45:04,090. Led Zeppelin - Rock and Roll"
t = "MH,Metal Heart Radio,2022-01-14 18:45:04,090. Led Zeppelin, special guest - Rock and Roll"

vysledek = t.split(",", maxsplit=3)
print(vysledek[3])


from collections import Counter
import re
import pandas

#with open('radiohead.csv', encoding="utf-8") as file:
    #seznam=file.read()

seznam = pandas.read_csv('radiohead.csv')
print(seznam)

beat = [seznam['station']]
print(beat)
if beat == "Rádio Beat":
    for one_song in seznam['title']:
        print(seznam['title'])
    else:
        