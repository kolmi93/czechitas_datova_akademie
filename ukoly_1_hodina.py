# ÚKOL Č. 1 - # Sem přidej kód, který proměnnou cislo zvýší o 1
cislo = 100
print(cislo)
cislo +=1
print(cislo)

# ÚKOL Č.2 - ulož do proměnné číslo od uživatele a pak zadej kó, který zvýší číslo o 1
cislo_2 = int(input("Vyberte si libovolné číslo:\n"))
print (cislo_2)
cislo_2 +=1
print(cislo_2)

# ÚKOL Č.3 - převod ze stupňů Fahrenheita na Celsia
fahrenheit = int(input("Na kolik stupňů máte dle receptu rozehřát troubu ve stupních Fahrenheita?\n"))
prevod = round((5*(fahrenheit-32))/9)
print(f"Pokud máte troubu rozehřát na {fahrenheit} stupňů Fahrenheita, znamená to, že trouba musí být rozehřátána {prevod} stupňů Celsia.")

# PROCVIČOVÁNÍ ÚKOLŮ Z PRVNÍ HODINY:

# ÚKOL Č. 1: Napiš kód, který zpracuje seznam čísel a vypíše jejich součet (bez použití funkce sum()).
input = [1,2,3,4,5,6,7,8,9]

sum_of_numbers = 0
for one_numer in input:
    sum_of_numbers += one_numer
print(sum_of_numbers)

# ÚKOL Č. 2: Napiš kód, který zpracuje seznam čísel a vypíše největší prvek v tomto seznamu (bez použití funkce max()).
input_2 = [1,2,3,352,4,5,6,7,8,9]

max_number = 0
for one_number_2 in input_2:
    if one_number_2 > max_number:
        max_number=one_number_2
print(max_number)

# ÚKOL Č. 3: Napiš kód, který zpracuje seznam čísel a vypíše pouze sudá čísla z tohoto seznamu.
input_3 = [1,2,3,4,5,6,7,8,9]

suda = 0
for one_number_3 in input_3:
    if one_number_3 % 2 == 0:
        print(one_number_3)

# ÚKOL Č. 4: Napiš kód, který zpracuje seznam čísel a vytvoří nový seznam se sudými čísly a nový seznam s lichými čísly z původního seznamu.
input_4 = [1,2,3,4,5,6,7,8,9]
suda = []
licha = []

for one_number_4 in input_4:
    if one_number_4 % 2 == 0:
        suda.append(one_number_4)
    else:
        licha.append(one_number_4)

print(suda)
print(licha)

# ÚKOL Č. 5: Napiš kód, který zpracuje seznam a vytvoří nový seznam bez duplikátů. Výsledné pořadí prvků musí být zachováno.
input_5 = [1,3,2,4,5,9,7,8,6,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]

out_put = []

for one_number_5 in input_5:
    if one_number_5 not in out_put:
        out_put.append(one_number_5)

print(out_put)

# ÚKOL Č. 6: Při přihlašování na střední školu mohou být důležitější příklady z některých konkrétních předmětů. Uprav kód z lekce tak, aby spočítal průměr pouze z jazyků, matematiky a fyziky.
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

choice = school_report[0] + school_report[1] + school_report[2] + school_report [5]
count = str(choice[1] + choice [3] + choice [5] + choice [7])
total = int(count)/int(len(choice)/2)
print(f"Průměrná známka z vybraných předmětů u žáka XY je: {total}).")

sum_of_marks = 0
count_of_marks = 0
for row in school_report:
    if row[0] in ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]:
        sum_of_marks = sum_of_marks + row[1]
        count_of_marks = count_of_marks + 1
print(sum_of_marks/count_of_marks)

# ÚKOL Č. 7:  Kolik přišlo mužů a kolik žen? Kdy se narodil nejstarší a kdy nejmladší pacient? Pokud nevíš, jak funguje rodné číslo, vysvětlení je níže: Rodné číslo je identifikační číslo, které slouží k jednoznačné identifikaci osoby. V České republice se rodné číslo skládá z 10 číslic a jednoho lomítka, které ho rozděluje na části. Prvních 6 číslic udává datum narození v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice). Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202. Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby. Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě.
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]

zeny = 0
muzi = 0
for vyber in rodna_cisla:
    mesic = vyber[2]+vyber[3]
    if int(mesic) > 50:
        zeny = zeny + 1
    else:
        muzi = muzi + 1
print(f"Ve vybraný den navšívilo {zeny} žen a {muzi} mužů lékařovu ordinaci.")

nejmladsi = max(rodna_cisla)
nejstarsi = min(rodna_cisla)
print(f"Nejmladším pacientem lékaře byl ve vybraný den pacient s rodnym číslem: {nejmladsi}.")
print(f"Nejstarším pacientem lékaře byl ve vybraný den pacient s rodnym číslem: {nejstarsi}.")