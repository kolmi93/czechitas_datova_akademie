#def secti (a,b):
#    return a+b
#vysledek = secti(3,4)
#print(vysledek)

#def secti_2(a: int, b: int) -> int:
#    return a+b

#vysledek=secti_2(3, 7)
#print(vysledek)

#def nacti_soubor(nazev_souboru):   
#    vysledek=[]
#    with open(nazev_souboru, encoding="utf-8") as f:
#        for line in f:
#            vysledek.append(line.strip())
#    return(vysledek)

#print(len(nacti_soubor("radiohead.csv")))

vstupni_data = [
    "iOS",
    "Android",
    "Windows",
    "Android",
    "Android",
    "iOS",
    "Android",
    "iOS",
    "Android",
    "Windows",
    "Android",
    "Windows",
    "Android",
    "Windows",
    "Android",
    "Windows",
    "Android",
]

citac_slovnik = {}

for platforma in vstupni_data:
    if platforma in citac_slovnik:
        citac_slovnik[platforma] += 1
    else:
        citac_slovnik[platforma] = 1
print(citac_slovnik)


from collections import Counter

citac_counter = Counter()
for platforma in vstupni_data:
    citac_counter[platforma] += 1
print(citac_counter)
