import pandas as pd
import json

# načtení pomocí pandas read_csv a sep - pro konktolu (lepší přehled)
netflix_přehled = pd.read_csv('netflix_titles.tsv', sep='\t')
# print(netflix_přehled)
# print(netflix_přehled.columns)

lines=[]
with open ('netflix_titles.tsv', encoding='utf-8') as file:
    for line in file:
        lines.append(line.strip()) # odstraní mezery na koncích a začátcích stringu

# do listu se nahrajou jednotlivé slovníky
final = []

# jednotlivé slovníky:
for data in lines[1:]: # hranatá závorka vypíše vše, co je od 1. řádku dál
    column = data.split('\t') # split definuje, na čem se jednotlivé sloupce rozdělují - rozseá text
    
    primary_title = {} # tvorba jednotlivých slovníků. Těmi se pak naplní final
    primary_title['title'] = column[2]
    lines.append(primary_title)

    director = {} # tvorba jednotlivých slovníků. Těmi se pak naplní final
    director['director'] = column[15]
    lines.append(director)

    cast = {}
    cast['cast'] = column[16]
    lines.append(cast)

    genres = {}
    genres['genres'] = column[8]
    lines.append(genres)

    decade = {}
    if int(column[5]) >= 1970 and int(column[5]) < 1980:
        decade['decade'] = '1970'
    elif int(column[5]) >= 1980 and int(column[5]) < 1990:
        decade['decade'] = '1980'
    elif int(column[5]) >= 1990 and int(column[5]) < 2000:
        decade['decade'] = '1990'
    elif int(column[5]) >= 2000 and int(column[5]) < 2010:
        decade['decade'] = '2000'
    elif int(column[5]) >= 2010 and int(column[5]) < 2020:
        decade['decade'] = '2010'
    elif int(column[5]) >= 2020 and int(column[5]) < 2030:
        decade['decade'] = '2020'
    else:
        decade['decade'] = '2030'
    lines.append(decade)

print(lines)

# print(netflix_přehled.columns) # přehled názvu sloupců

with open ('Kolarova_Michaela_2.py', mode='w', encoding='utf-8') as file:
    json.dump(final, file, indent=4)