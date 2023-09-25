polozka = ["čajová konička s hrnky", 899, True]
# výpis datového typu - 'list'
print(type(polozka))

polozka_2= "čajová konvička s hrnky", 899, True
# výpis datového typu - 'tupple'
print(type(polozka_2))

title, price, in_stock = polozka_2
print(title)
print(price)
print(in_stock)

names = set()
names.add("Marcela")
names.add("Jana")
names.add("Honza")
names.add("Marcela")
print(names)
print(len(names), names)

# prevod seznamu na množinu
# Vytvořím seznam
jmena = ["Marcela", "Petra", "Marcela"]
print(jmena)
# Převod na množinu
jmena_unikatni = set(jmena)
# Množina má jenom dvě položky - máme dvě unikátní jména
print(jmena_unikatni)

item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
# Přečteme hodnotu podle klíče
description = item["title"]
# Upravujeme hodnotu pomocí klíče - nastavíme cenu 950
item["price"] = 950
# Přidávám nový klíč - weight
item["weight"] = 0.6
print(f"Název položky je {item['title']}")
if "weight" in item:
    print(f"Hmotnost je {item['weight']} kg.")
else:
    print("Hmotnost není uvedena.")

sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
# výpis jen klíčů za s sebou
for key in sales:
    print(key, end=", ")

for key, values in sales.items():
    print(key)
    print(values)
    print(f"Knihy '{key}' bylo prodáno {values} ks.")

sales_value = sales.values()
print(sales_value)