#7578
dict_tovarov = {}
file = "26-153.txt"
with open(file, "r") as file : #with в любом случае закроет файл "r" read только читает файл as file
    # cоздаёт переменную, с которой можно взаимодействовать
    kol_vo_tovarov = int(file.readline()) #читает первую строку
    d = [line.split() for line in file] #создаёт список где каждая строка из файла разбивается на
    # отдельные элементы (по пробелам).

items = [(int(article), int(price), int(status)) for article, price, status in d ]


full_price = sum(item[1] for item in items )
average_price = full_price / kol_vo_tovarov #cредняя цена

expensive_items = [item for item in items if item[1] > average_price] #тут только дорогие товары отбираем

sales = {}
for article, price , status in expensive_items:
    if article not in sales:
        sales[article] = [0, 0, price] # [продано, осталось, цена]
    elif status == 0 :
        sales[article][0] += 1 # Продано
    else:
        sales[article][1] += 1 # Осталось

'''Сортировка:
Сначала по количеству проданных единиц (по убыванию).
Затем по цене (по убыванию).
Потом по количеству оставшихся единиц (по возрастанию)'''
sorted_dict = sorted(sales.items(), key = lambda f: (-f[1][0], -f[1][1], -f[1][2]))

leader_article, (sold, remaining, price) = sorted_dict[0]

# Шаг 5: Суммарная стоимость оставшихся единиц
total_value = remaining * price

# Шаг 6: Вывод результата
print(f"Ответ: {total_value} {leader_article}")

