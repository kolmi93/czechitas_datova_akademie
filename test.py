fruit_sales = [
    {"fruit": "apple", "quantity": 30, "price_per_unit": 1.2},
    {"fruit": "orange", "quantity": 45, "price_per_unit": 0.8},
    {"fruit": "banana", "quantity": 25, "price_per_unit": 0.6},
    {"fruit": "grape", "quantity": 40, "price_per_unit": 2.5},
]

total_price = []
for one_fruit in fruit_sales:
    print(one_fruit['quantity'])
    print(one_fruit['price_per_unit'])
    total = one_fruit['quantity'] * one_fruit['price_per_unit']
    total_price.append(total)
print(sum(total_price))
print(f'Celková tržba za ovoce je {sum(total_price)} Kč.')
print(f'Přičemž tržba z jablek činí {round(total_price[0])} Kč, pomerančů {round(total_price[1])} Kč, banánů {round(total_price[2])} Kč a hroznů {round(total_price[3])} Kč.')

# č.3:
# Napiš příkaz, který zjistí z proměnné d počet koníčků dané osoby a uloží ho do proměnné count_hobbies. 
d = {
    "firstName": "Jane",
    "lastName": "Doe",
    "hobbies": ["running", "sky diving", "singing"],
    "age": 35,
    "children": [
        {
            "firstName": "Alice",
            "age": 6
        },
        {
            "firstName": "Bob",
            "age": 8
        }
    ]
}

# print(d['hobbies'])
count_hobbies = len(d["hobbies"])
print(count_hobbies)

# Č.4:
# Pro zadanou proměnnou w: w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# Napiš výraz, který vrátí seznam pracovních dnů, tedy [“Monday”, “Tuesday”, “Wednesday”, “Thursday”, “Friday”].

w = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
work_days = w[:5]
print(work_days)