names = ['Roman', 'Radek', 'Jana','Petra']
with open ('zapis.txt', mode='w', encoding='utf=8') as output_file:
    for name in names:
        print(name, file=output_file)

text = "Tento text se uloží do souboru."
with open ('text.txt', mode='w', encoding='utf=8') as output_file:
    print(text, file=output_file)
