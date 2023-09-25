import statistics
# Seznam teplot jako desetinná čísla
temperatures = []
with open("mereni.txt", encoding="utf-8") as file:
    # Čteme soubor řádek po řádku
    for line in file:
        # Odstranění zalomení řádků
        line = line.strip()
        # Rozdělení na dvě položky v seznamu
        line = line.split("\t")
        # Převod teploty na číslo
        temp = float(line[1])
        # Uložím si den
        day = line[0]
        # Přidám to do seznamu temperatures jako vnořený seznam
        temperatures.append([day, temp])
# Výsledkem je dvourozměrný seznam
print(temperatures)

lines=[]
celkem_rok = 0
hodina = int(input("Jaká je Vaše hodinová mzda?:\n"))
with open("vykaz.txt", encoding="utf-8") as file_2:
    for line in file_2:
        # Odstranění zalomení řádků
        line = int(line)
        lines.append(line)
        celkem_rok = int(celkem_rok + hodina*line)
        prumer_mesic = int(celkem_rok/12)
print(f"Za rok vyděláte: {celkem_rok} Kč.")
print(f"Za měsíc vyděláte průměrně: {prumer_mesic} Kč.")

radky = []
radek_slova = []
radek_cislo = 1
with open ('pocet-slov_praha.txt', encoding="utf-8") as file_3:
    for radek in file_3:
        radek = radek.split()
        print(f"Řádek č. {radek_cislo} má {len(radek)} slov.")
        radek_cislo = radek_cislo + 1
        radek_slova.append(len(radek))
print(f"Celý text má {sum(radek_slova)} slov.")