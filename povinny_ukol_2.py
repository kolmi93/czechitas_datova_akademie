import json

lines=[]
with open ('netflix_titles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line.strip()) # odstraní mezery na koncích a začátcích stringu

# do listu se nahrajou jednotlivé slovníky
final = []

# jednotlivé slovníky:
for data in lines[1:]: # hranatá závorka vypíše vše, co je od 1. řádku dál
    column = data.split('\t') # split definuje, na čem se jednotlivé sloupce rozdělují - rozseká text

    primary_title = {} # tvorba jednotlivých slovníků. Těmi se pak naplní final
    primary_title['title'] = column[2]
    final.append(primary_title)

    direct = (column[15]).split(',')
    d = list(filter(None, direct))
    primary_title['director'] = d
    final.append(primary_title)

    ca = (column[16]).split(',')
    c = list(filter(None, ca))
    primary_title['cast'] = c
    final.append(primary_title)

    gen = (column[8]).split(',')
    primary_title['genres'] = gen
    final.append(primary_title)

    if int(column[5]) >= 1970 and int(column[5]) < 1980:
        primary_title['decade'] = '1970'
    elif int(column[5]) >= 1980 and int(column[5]) < 1990:
        primary_title['decade'] = '1980'
    elif int(column[5]) >= 1990 and int(column[5]) < 2000:
        primary_title['decade'] = '1990'
    elif int(column[5]) >= 2000 and int(column[5]) < 2010:
        primary_title['decade'] = '2000'
    elif int(column[5]) >= 2010 and int(column[5]) < 2020:
        primary_title['decade'] = '2010'
    elif int(column[5]) >= 2020 and int(column[5]) < 2030:
        primary_title['decade'] = '2020'
    else:
        primary_title['decade'] = '2030'
    final.append(primary_title)

with open ('Kolarova_Michaela_2.py', mode='w', encoding='utf-8') as file:
    json.dump(final, file, indent=4)