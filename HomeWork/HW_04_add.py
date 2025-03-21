# ------------------------------ЗАНЯТИЕ 4 (Структуры данных. Доп задания)------------------------------

#1. Магазин -----.
# Есть словарь с товарами.
# Необходимо увеличить цену всех продуктов на 20 процентов.
# Удалить товар “milk”.
# Добавить товар “Salt” с количеством 7 и ценой 12.
# Вывести общую стоимость всех товаров в магазине.
# Ответ: 6516.0
#
# products = {
#      "apple": {"quantity": 10, "price": 100},
#     "banana": {"quantity": 20, "price": 50},
#     "orange": {"quantity": 15, "price": 80},
#     "grape": {"quantity": 8, "price": 120},
#     "milk":{"quantity": 12, "price": 90},
#      "bread": {"quantity": 30, "price": 40}
# }
# for item in products.values():
#     item["price"] *=1.2
#
# del products["milk"]
#
# products["salt"] = {"quantity": 7, "price": 12}
# print(products)
#
# total = 0
# for item in products.values():
#     total += item["quantity"] * item["price"]
# print(total)


#2. Alice --------------------------------------------------------------------
# Есть два списка одинаковой длины.
# Создайте словарь info из ключей keys и значений values.
# (Каждое значение занимает ту же позицию, что и ключ в другом списке)
# Выведите словарь info на экран.

# keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
# values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]
#
# new_dict = dict(zip(keys, values))
# print(new_dict)

#3. Шифр --------------------------------------------------------------------
# Есть сообщение (строка):
# "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
# И ключ к шифру, где каждую букву нужно заменить на ее значение в словаре: cipher.
#
# Расшифруйте секретное сообщение с помощью ключа cipher,
# при этом мусорные значение (которых нет в словаре) должны быть пропущены
# и не добавлены в результат.
# Выведите результат на экран.
# Дополнительно: напишите программу, которая получает строку через ввод с клавиатуры
# и “отправляет” зашифрованный ответ агенту.

cipher = {
    "а": "щ", "б": "д", "в": "ю", "г": "ф", "д": "з", "е": "м", "ё": "р",
    "ж": "т", "з": "п", "и": "я", "й": "с", "к": "н", "л": "э", "м": "к",
    "н": "л", "о": "ё", "п": "ж", "р": "ц", "с": "б", "т": "у", "у": "в",
    "ф": "о", "х": "и", "ц": "х", "ч": "г", "ш": "е", "щ": "й", "ъ": "ы",
    "ы": "ч", "ь": "ш", "э": "ъ", "ю": "а", "я": "ь"
}

str = "2__234йшDGмёшSDFжкъrrrщзнSDF78юкйфуSDFшёью$#2Sшжйи3%узфsdf34нкфыvvя"
#
# lst = []
#
# for el in str:
#     if el in cipher.keys():
#         lst.append(cipher[el])
# print(*lst) # расшифрованное сообщение

# str2 = input()
# lst2 = []
#
# for el in str2:
#     for key, value in cipher.items():
#          if el == value:
#              lst2.append(key)
#
# print(''.join(lst2)) # засшифрованное сообщение в виде строки


#4. Самая популярная буква --------------------------------------------------------------------
# Есть строка: dialog.
#  - С помощью словаря подсчитайте количество букв в строке dialog игнорируя регистр.
# Ключами в словаре должны быть буквы, а значения - количество вхождения буквы в текст.
# Например: {'т': 26, 'е': 32...}
#
#  - Вывести на экран букву, которая встречается максимальное количество раз.

dialog = """Doc: Запомни! Согласно моей теории, ты помешал знакомству своих родителей.
Если они не встретятся, то не влюбятся, не поженятся, и у них не будет детей.
Поэтому твой старший брат исчезает с фотографии. Затем очередь твоей сестры,
и если ты все не исправишь, ты будешь следующим.
Marty: Тяжелый случай.
Doc: Вес тут совершенно ни при чем. """

keys = []
values = []

dialog_low = dialog.lower()

for el in dialog_low:
    if el.isalpha():
        keys.append(el)
        value = dialog_low.count(el)
        values.append(value)

info = dict(zip(keys, values))
print(info)

max_value = max(info, key = info.get) # ищем букву, которая чаще всего встречается
print(max_value)






















