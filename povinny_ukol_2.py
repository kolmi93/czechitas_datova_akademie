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

    direct = (column[15]).split(',')
    d = list(filter(None, direct))
    primary_title['director'] = d

    ca = (column[16]).split(',')
    c = list(filter(None, ca))
    primary_title['cast'] = c

    gen = (column[8]).split(',')
    primary_title['genres'] = gen
    
    choice = column[5].split(',')
    time =  int("".join(choice))
    if time % 10 == 0:
        time = time
    else:
        time = time - time % 10
    primary_title['decade'] = time
    final.append(primary_title)

with open ('movies.json', mode='w', encoding='utf-8') as file:
    json.dump(final, file, indent=4, ensure_ascii = False)