# ÚKOL Č.1
school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# Napiš program, který spočte průměrnou známku ze všech předmětů.
total = 0
for item, values in school_report.items():
    total = total + values
    prumer = total/len(school_report)
print(f"Průměrná známka ze všech předmětů je: {prumer}.")

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.
for item, value in school_report.items():
    if value == 1:
        print(item)

# ÚKOL Č.2
books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]
# Napiš program, který spočte celkový počet stran, které Gustav přečetl.
pocet_stran = 0
for kniha in books:
    pocet_stran = pocet_stran + kniha['pages']
print(pocet_stran)

# Připiš do programu výpočet počtu knih, kterým dal Gustav hodnocení alespoň 8.
pocet_stran = 0
for kniha in books:
    if kniha['rating'] >=8:
        pocet_stran = pocet_stran + kniha['pages']
print(pocet_stran)

# ÚKOL Č.3
plates = {"4A2 3000": "František Novák",
    "6P5 4747": "Jana Pilná",
    "3B7 3652": "Jaroslav Sečkár",
    "1P5 5269": "Marta Nováková",
    "37E 1252": "Martina Matušková",
    "2A5 2241": "Jan Král"}
# V následujícím slovníků je evidence automobilů. Klíčem jsou státní poznávací značky (SPZ) a hodnotou je jméno majitele vozu. Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.
for key, value in plates.items():
    if key[1] == "P":
        print(value)

# ÚKOL Č.4
import math
recept = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

# Uložte si tuto strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
total = 0
for item in recept['ingredience']:
    price = item[-1].split(" ")[0]
    price = float(price)
    total = math.ceil(total + price)
print(total)