from collections import Counter


# Protože jsme na začátku lekce napsali načtení souboru do seznamu jako funkci, tak ji tady použiju:
# Takže: def jako definuji, nacti_soubor je mnou zvolený název funkce.
# Ta dostává 1 proměnnou: nazev_souboru typu str (řetězec)
# A 1 proměnnou vrací (->): té se v záhlaví žádný název neuvádí, ale bude typu list (seznam)
def nacti_soubor(nazev_souboru: str) -> list:
    # založím si prázdný seznam s názvem vysledek
    vysledek = []
    # otevřu soubor s názvem nazev_souboru v kódování UTF-8 (u konkrétního souboru zjistím např. ve VSCode vpravo dole)
    # a otevřený soubor si označím jako f
    with open(nazev_souboru, encoding="utf8") as f:
        # pro každý řádek v souboru f (který si označím jako radek)…
        for radek in f:
            # …vlož proměnnou radek do seznamu vysledek. Na radek volám funkci strip, která mi odstraní symboly konce řádků
            vysledek.append(radek.strip())
    # jako výsledek volání funkce nacti_soubor vrať proměnnou vysledek = seznam obsahující všechny řádky v daném souboru
    return vysledek


# a po celé té definici, tady tu funkci zavolám, tzn. otevřu soubor radiohead.csv a do proměnné data uložím výsledek,
# kterým je seznam jednotlivých řádků v daném souboru
data = nacti_soubor("radiohead.csv")
print(data)
# připravím si prázdný čítač, syntaxi s kulatými závorkami si bohužel musím pamatovat.
# (technicky, pro pokročilé: syntaxe bla = Trida() mi do proměnné bla uloží nový objekt třídy Trida, v tomto případě tedy nový objekt Counter)
citac = Counter()

# projdu všechny položky v seznamu data kromě prvního řádku se záhlavím (code,station,time,title)
# který jsem odřízl tzv. slicem, to je to [1:] = vše od 2. prvku do konce seznamu
for zaznam in data[1:]:
    # rozdělit celý řádek:
    # RB,Rádio Beat,2022-01-14 18:35:03,THIN LIZZY - THE BOYS ARE BACK IN TOWN
    # na seznam jednotlivých „sloupců“ podle čárek. výsledkem je následující seznam:
    # [0] => RB
    # [1] => Rádio Beat
    # [2] => 2022-01-14 18:35:03
    # [3] => THIN LIZZY - THE BOYS ARE BACK IN TOWN
    # argument maxsplit=3 zajistí, že výsledek bude mít max 4 prvky (ale může jich mít i méně!)
    sloupce = zaznam.split(",", maxsplit=3)
    
    # pokud se hodnota v druhém sloupci NEROVNÁ řetězci "Rádio Beat"…
    if sloupce[1] != "Rádio Beat":
        # 👉 zbytek for cyklu vynechám a pokračuji na další záznam, na další položky v seznamu data 👈
        # 👉 continue = super důležitá konstrukce 👈
        continue

    # Pozn.: Protože mám uvnitř ifu continue, do bloku ohraničeného rukama 👇👆 se dostanu jen, pokud if neplatí.
    # Je to, jako bych napsal else, jen teď nemusím celý zbytek kódu odsadit, bude se to líp číst
    # a lépe se s tím pracuje.

    # 👇👇👇

    # název interpreta a skladby ze čtvrtého sloupce uložím do proměnné titulek
    titulek = sloupce[3]
    # a opět rozdělím, tentokrát podle sekvence „mezera pomlčka mezera“, a to max. jednou
    # (pokud se „ - “ v titulku nevyskytuje, výsledkem bude seznam o 1 prvku s indexem 0)
    titulek_zvlast = titulek.split(" - ", maxsplit=1)
    # do proměnné interpret si uložím prvek z první pozice, tj. název interpreta
    interpret = titulek_zvlast[0]
    # v datech je bordel, jingly jsou označené jako Radio BEAT - Classic Rock
    # pokud na takovou položku narazím…
    if interpret == "Radio BEAT":
        # …opět ji pomocí continue přeskočím
        continue

    # V čítači typu Counter si „udělám čárku“ k danému interpretovi. Counter se chová jako slovník,
    # takže k prvkům uvnitř přistupuji přes hranaté závorky. Pokud tam ale prvek není, při inkrementaci
    # (operátor += 1) se založí a nastaví na hodnotu 1. Na rozdíl od slovníku tedy nemusím jednotlivé
    # položky zakládat ručně sámˇv nějakém ifu.
    citac[interpret] += 1

    # 👆👆👆

# Pozn.: Tohle je nový for cyklus, ten se provede bez ohledu na volání continue výše. Sem prostě dojdu vždycky. 👍
print(citac)
# A tohle je další výhody typu Counter: metoda most_common(n) mi vrátí n nejčastějších položek v daném čítači.
# Takže je jen projdu for cyklem, vypíšu a mám vystaráno! 🥳
#for item in citac.most_common(10):
#    print(item)