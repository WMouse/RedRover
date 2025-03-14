# ------------------------------ЗАНЯТИЕ 4 (Структуры данных)------------------------------
#1. Особые числа -----
#Генерируем список из чисел в диапазоне от 0 до 100 включительно,
# которые делятся без остатка как на 2, так и на 3. Двумя способами

# numbers = [] # обычный способ
# for i in range(100):
#     if i % 2 == 0 and i % 3 == 0:
#         numbers.append(i)
# print(numbers)

# numbers = [i for i in range(100) if i % 2 == 0 and i % 3 == 0] # генератор списка
# print(numbers)

#2. Фильтр -----
# items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
# summ = 0
# for i in items:
#     if type(i) == int or type(i) == float:
#         summ += i
# print(summ)

#3. История сообщений -----
# messages = []
#
# while True:
#     print('Введите сообщение: ')
#     msg = input()
#
#     if len(messages) >= 5:
#         del messages[0]
#
#     messages.append(msg)
#
#     if msg == 'Пока':
#         print('Ну ладно, пока!')
#         print(messages)
#         break

#4 Рефакторинг кода
# age = 16
# admin = True
# if age >= 18 or admin == True:
#     print("Доступ разрешен!")
# else:
#     print("Доступ запрещён!")
