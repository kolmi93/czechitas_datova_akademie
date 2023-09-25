#ÚKOL Č. 1
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open ('kalendar.txt', mode='w', encoding='utf-8') as output_file:
    for den in pocty_dni:
        print(den, file=output_file)

# ÚKOL Č.2
nazev = input("Jak se bude Váš soubor jmenovat?\n")
zapis = input("Co má v tomto souboru být napsáno?\n")

with open(nazev, mode='w', encoding='utf-8') as output_file:
    print(zapis, file=output_file)

# ÚKOL Č. 3
