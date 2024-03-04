import pandas as pd

# nacteni data
data = pd.read_csv('netflix_imdb_test.tsv', sep='\t')
# print(data)
# print(data['PRIMARYTITLE'])

total = 0
for character in data['PRIMARYTITLE']:
    #print(character)
    total += len(character)
print(total)

#print(f'Ve sloupci PRIMARYTITLE je celkem {total} znaků.')