sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}

books = [
    {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
    {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
    {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
]

# Zkusme si ještě spočítat tržby nejen v prodaných kusech, ale i v penězích. Vždy tedy počet prodaných knih (hodnota s klíčem sold) vynásobíme cenou jedné knihy (hodnota s klíčem price).
income = 0
for item in books:
    income = income + item['sold']*item['price']
print(f"celkem bylo prodáno knih v hodnodě {income} Kč.")

# Zkusme ještě jednu úpravu. Nakladatele zajímá, jaké jsou peněžní tržby za knihy vydané v roce 2019. U každé knihy tedy musíme zkontrolovat, zda vyšla v roce 2019, a pouze pokud je tato podmínka splněná, přičteme tržbu za knihu k proměnné total_sales
inc = 0
for item in books:
    if item['year'] == 2019:
        inc = inc + item['sold']*item['price']
print(f"celkem bylo v roce 2019 prodáno knih v hodnodě {inc} Kč.")