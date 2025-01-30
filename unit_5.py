# def red():
#     return 'Color is red'
#
#
# def green():
#     return 'Color is green'
#
#
# def blue():
#     return f'Color is blue'
#
#
# colors = {}
# colors[green] = '00FF00'
# colors[blue] = '0000FF'
# colors[red] = 'FF0000'
#
# for i in colors:
#     print(f'{i()} - {colors[i]}')
from collections import defaultdict


# cache = {}
#
#
# def fact(n):
#     if cache.get(n):
#         return f'Get from cache value fact({n})\n{cache[n]}'
#     else:
#         total = 1
#         for i in range(1, n + 1):
#             total *= i
#         cache.setdefault(n, total)
#     return total


# exchange_rates = {
#     "USD": 1.0,
#     "EUR": 0.861775,
#     "GBP": 0.726763,
#     "INR": 75.054725,
#     "AUD": 1.333679,
#     "CAD": 1.237816,
#     "SGD": 1.346851,
# }
#
#
# def convert(currency_from: str, currency_to: str, summ: int) -> float:
#     return round(summ * exchange_rates[currency_to] / exchange_rates[currency_from], 2)
#
#
# currency = convert("GBP", "USD", 100)
# print(currency)


# square = lambda x, y: x**2 + y**2


# adding_10 = lambda x: x + 10


# starts_with = lambda str: str.startswith('W')


# check_word = lambda str: (
#         (str.upper().startswith('Q') or str.upper().startswith('R')) and str[-1].upper() in ['A', 'E', 'I', 'U', 'O']
# )


# def is_leap(year: int) -> bool:
#     return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


# is_leap = lambda year: year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


# sale_lambda = lambda x: x * 0.9


# sale_lambda = lambda x: x * 0.9 if x > 50 else x


# average = lambda *args: sum(args) / len(args)


# def print_results(lst: list[tuple]):
#     for i in sorted(lst, key=lambda x: x[1]):
#         print(*i)
#
#
# marks = [('English', 88), ('Science', 100), ('Maths', 81),
#          ('Physics', 100), ('History', 82), ('Music', 100)]
# print_results(marks)


# def print_results(lst: list[tuple]):
#     for i in sorted(lst, key=lambda x: -x[1]):
#         print(*i)
#
#
# marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
# print_results(marks)


# def print_results(lst: list[tuple]):
#     temp_lst = sorted(lst, key=lambda x: x[0].lower())
#     for i in sorted(temp_lst, key=lambda x: x[1], reverse=True):
#         print(*i)
#
#
# marks = [('english', 100), ('Science', 100), ('maths', 100),
#          ('Physics', 100), ('history', 100), ('Music', 100)]
# print_results(marks)


# def print_results(lst: list[tuple]):
#     temp_lst = sorted(lst, key=lambda x: x[0].lower(), reverse=True)
#     for i in sorted(temp_lst, key=lambda x: x[1], reverse=True):
#         print(*i)
#
#
# marks = [('English', 88), ('Science', 90), ('Maths', 88),
#          ('Physics', 93), ('History', 78), ('French', 78),
#          ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
# print_results(marks)
# print('-' * 20)
# marks = [('english', 100), ('Science', 100), ('maths', 100),
#          ('Physics', 100), ('history', 100), ('Music', 100)]
# print_results(marks)


# def get_sort_lines(lst: list[tuple]):
#     temp_lst = sorted(lst, key=lambda x: (x[0], x[1]))
#     return sorted(temp_lst, key=lambda x: (x[1] - x[0]) if x[1] > x[0] else (x[0] - x[1]))
#
#
# lines = [(-4, 4), (2, 3), (5, 9), (-1, -3)]
# print(get_sort_lines(lines))
# print('-' * 20)
# lines = [(5, 4), (2, 3), (1, 0), (-1, -2)]
# print(get_sort_lines(lines))
# print('-' * 20)
# lines = [(5, 6), (5, 4), (1, 0), (0, -1), (1, 2), (2, 1)]
# print(get_sort_lines(lines))


# def print_goods(lst: list[dict]):
#     for item in sorted(lst, key=lambda x: (x['color'].lower(), -x['model'])):
#         print(f"Производитель: {item.get('make')}, модель: {item.get('model')}, цвет: {item.get('color')}")
#
#
# models = [{'make': 'Nokia', 'model': 2, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 3, 'color': 'red'},
#           {'make': 'Samsung', 'model': 5, 'color': 'Yellow'},
#           {'make': 'Apple', 'model': 10, 'color': 'RED'},
#           {'make': 'Oppo', 'model': 9, 'color': 'Red'},
#           {'make': 'Huawei', 'model': 4, 'color': 'BLACK'},
#           {'make': 'Honor', 'model': 3, 'color': 'black'},
#           {'make': 'Nothing Phone', 'model': 7, 'color': 'Yellow'}]
# print_goods(models)


# def print_goods(lst: list[str]):
#     new_lst = []
#     for item in lst:
#         name, price = item.split(': ')
#         price = float(price)
#         new_lst.append((price, name))
#     new_lst.sort(key=lambda x: (-x[0], x[1].lower()))
#     for price, name in new_lst:
#         print(f'{price:.2f} - {name}')
#
#
# data = [
#     'a: 1',
#     'aa: 2',
#     'aA: 3',
#     'Aa: 4',
#     'Aa: 5',
#     'AA: 5',
#     'aa: 5',
#     'aA: 5',
# ]
# print_goods(data)


# def print_best_and_worst_laureate(my_dict: dict[str, str]) -> None:
#     new_dict = {}
#     for v in my_dict.values():
#         if v in new_dict:
#             new_dict[v] += 1
#         else:
#             new_dict[v] = 1
#     best_name = max(new_dict, key=lambda x: new_dict[x])
#     best_count = new_dict[best_name]
#     worst_name = min(new_dict, key=lambda x: new_dict[x])
#     worst_count = new_dict[worst_name]
#     print(best_name, best_count, sep=', ')
#     print(worst_name, worst_count, sep=', ')
#
#
# laureates = {'Премия «Оскар» за лучшую мужскую роль': 'Tom Kruize'}
#
# print_best_and_worst_laureate(laureates)

# def print_order_rating(lst: list[tuple[str, int]]) -> None:
#     new_dict = {}
#     for item in lst:
#         name, count = item[0], item[1]
#         if name in new_dict:
#             new_dict[name].append(count)
#         else:
#             new_dict[name] = [count]
#     for k, v in new_dict.items():
#         avg = sum(v) / len(v)
#         new_dict[k] = avg
#     for name, count in sorted(new_dict.items(), key=lambda x: (-x[1], x[0].lower())):
#         print(name, count)
#
# drivers = [
#     ('Зина', 5),
#     ('Зина', 3),
#     ('Гермиона', 4),
#     ('Гермиона', 4),
#     ('александр', 4),
# ]
# print_order_rating(drivers)


# def print_statistic(lst: list[tuple[str, str]]) -> None:
#     new_dict = {}
#     for item in lst:
#         name, comment = item[0], item[1]
#         if name in new_dict:
#             new_dict[name].add(comment)
#         else:
#             new_dict[name] = {comment, }
#     for k, v in new_dict.items():
#         new_dict[k] = len(v)
#     for name, count in sorted(new_dict.items(), key=lambda x: (-x[1], x[0])):
#         print(f"Количество уникальных комментаторов у {name} - {count}")
#
# data = [
#     ('7', 'opushka'),
#     ('1', 'opushka'),
#     ('2', 'opushka'),
#     ('3', 'opushka'),
#     ('2', 'opushka'),
#     ('1', 'opushka'),
#     ('2', 'opushka'),
#     ('5', 'opushka'),
#     ('6', 'opushka'),
#     ('6', 'opushka'),
# ]
#
# print_statistic(data)
