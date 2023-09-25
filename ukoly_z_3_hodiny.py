# ÚKOL Č.1
# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu.
vysvedceni = {"cesky_jazyk":"3", "matematika":"2", "dejepis":"1"}
print(vysvedceni)

# ÚKOL Č. 2
sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# Přidej do slovníku nově vydanou detektivku "Noc, která mě zabila", která zatím nebyla uvedena na trh, je tedy prodáno 0 kusů
sales["Noc, která mě zabila"]=0
print(sales)

# U knihy "Vrah zavolá v deset" zvyš počet prodaných kusů o 100
sales["Vrah zavolá v deset"]+=100
print(sales)

# ÚKOL Č. 3
tombola = {
    7: "Láhev kvalitního vína Château Headache",
    15: "Pytel brambor z místního družstva",
    23: "Čokoládový dort",
    47: "Kniha o historii města",
    55: "Šiška salámu",
    67: "Vyhlídkový let balónem",
    79: "Moderní televizor",
    91: "Roční předplatné městského zpravodaje",
    93: "Společenská hra Sázky a dostihy",
}
# Napiš program, který se nejprve zeptá uživatele na číslo jeho lístku. Vstup uživatele si převeď na int
number=int(input("Jaké je číslo Vašeho lístku?\n"))
if number in tombola:
    print(f"Vyhráváš {tombola[number]}.")
else:
    print("Bohužel nevyhráváš nic.")

# ÚKOL Č.4
# Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name=input("Vítejte na večírku. Jaké je Vaše jméno?\n")
if name in passwords:
    heslo=input("Jaké je Vaše heslo?\n")
    if heslo == passwords[name]:
        print("Smíš vstoupit.")
    else:
        print("Vaše heslo není správné. Musíte odejít.")
else:
    print("Vaše jméno není na seznamu. Prosím, odejděte.")