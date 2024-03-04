import pandas as pd

# nacteni do dataframu data
data = pd.read_csv('netflix_imdb_test.tsv', sep='\t')
# print(data)
# print(data['PRIMARYTITLE'])

total = 0
for character in data['PRIMARYTITLE']:
    total += len(character)
print(total)