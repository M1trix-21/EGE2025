#7675
dict_shtraf = {}
#читает файл
file_path = "26-155.txt"
with open(file_path, "r") as file: #with в любом случае закроет файл "r" read только читает файл as file
    # cоздаёт переменную, с которой можно взаимодействовать
    n = int(file.readline().strip())  # кол-во наруш.

    # проходимся по каждой строке файла фором
    for line in file:
        # Считываем код машины, сумму штрафа и класс
        car_code, sum_shtraf, car_class = map(int, line.split())
        #мега мув с мап(для каждого объекта применяется: (функуия; объект к которому все это дело применят))

        key = (car_code, car_class) # создание кортежа, чтобы в последствии можно было сделать удобную работу с ними
        # так как кортежи можно запихнуть в 1 ключ и к нему всякие приколы (значение добавлять)

        # тута если ключик уже есть, то + сумма штрафов к нему иначе просто в словарь пихаем
        if key in dict_shtraf:
            dict_shtraf[key] += sum_shtraf
        else:
            dict_shtraf[key] = sum_shtraf

# Шаг 3: Сортировка данных по заданным условиям
sorted_dict_shtraf = sorted(dict_shtraf.items(),# Сортировка по сумме штрафов, коду машины и классу
                            key=lambda elem: (elem[1], elem[0][0], elem[0][1]),reverse=True
#сортировка по ключ значению понятна дальше можно сортировать еще и по первому и второму елементу ключа [0][0]
# и второй элемент [0][1]
)


max_payment = sorted_dict_shtraf[0]  # Берем первую запись из нашего sorted_dict_shtraf распаковываем кортежик
(car_code, car_class), total_fine = max_payment #(car_code, car_class) ключ значение total_fine= значение

# Шаг 5: Вывод результата f""  позволяет вставлять значения переменных в строку.
print(f"Ответ: {car_code} {total_fine}")
