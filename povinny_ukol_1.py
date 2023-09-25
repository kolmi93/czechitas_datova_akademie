import re
import json
from collections import Counter

with open('alice.txt', encoding ='utf-8') as file:
    alice = file.read()

# vyčíštění textu
upraveny = re.sub("\s", '', alice)
final = upraveny.lower()
print(final)

# počítání pomocí Counter()
new_alice = {}
new_alice = Counter(final)
print(new_alice)

# počítání pomocí vypsání
new_alice_2 = {}
for character in final:
    if character in new_alice_2:
        new_alice_2[character] +=1
    else:
        new_alice_2[character] = 1
print(new_alice_2)

with open('Kolarova_Michaela_1.py', 'w', encoding ='utf8') as json_file:
    json.dump(new_alice_2, json_file, ensure_ascii = True)