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


# def get_info_about_object(obj: object) -> None:
#     print(dir(obj))
#     print(f"Всего у объекта {len(dir(obj))} атрибутов и методов")
#
# def print_goods(lst):
#     pass
#
# print_goods.info = 'Функция для вывода информации о товарах'
# print_goods.is_working = False
# print_goods.status = 'Not ready'
#
# get_info_about_object(print_goods)


# def check_exist_attrs(obj: object, lst: list[str]) -> dict[str, bool]:
#     my_dict = {}
#     for i in lst:
#         my_dict[i] = hasattr(obj, i)
#     return my_dict
#
#
# def print_goods(lst):
#     pass
#
# print_goods.is_working = False
# print_goods.status = 'Not ready'
#
# print(check_exist_attrs(print_goods, ['is_working', 'status', 'time', 'speed']))


# def create_attrs(obj: object, lst: list[tuple[str, ...]]):
#     for i in lst:
#         setattr(obj, i[0], i[1])
#
#
# def print_goods(lst):
#     pass
#
# create_attrs(print_goods, [('is_working', False), ('days', 10), ('status', 'Not ready')])
#
# print(check_exist_attrs(print_goods, ['sort', 'is_working', 'days', 'status', 'upper']))


# def count_strings(*args) -> int:
#     count = 0
#     for i in args:
#         if isinstance(i, str):
#             count += 1
#     return count
#
# print(count_strings())


# def find_keys(**kwargs) -> list:
#     lst = []
#     for k, v in kwargs.items():
#         if isinstance(v, (tuple, list)):
#             lst.append(k)
#     return sorted(lst, key=lambda x: x.lower())
#
#
# print(find_keys(marks=[4, 5], name='Ashle', surname='Brown', age=20, Also=(1, 2)))
# print(find_keys(t=[4, 5], w=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
# print(find_keys(marks=[4, 5], ashle=[5], surname='Brown', age=20, Also=(1, 2)))
# print(find_keys(At=[4], awaited=(3,), aDobe=[5]))


# def outer() -> None:
#     def say_hello() -> None:
#         print('hello')
#
#     def say_bye() -> None:
#         print('bye')
#
#
#     say_hello()
#     say_bye()
#
# outer()


# def wrap_increment(value):
#     def _inc():
#         return value + 1
#     return _inc()
#
#
# print(wrap_increment(45))


# def get_extensions(file_list: list[str]):
#     def _get_extension(ext: str):
#         if "." in ext:
#             return ext.split(".")[-1]
#         else:
#             return ""
#     return [_get_extension(i) for i in file_list]
#
#
# print(get_extensions(["foo.txt", "bar.mp4", "python3"]))


# def double_odd_numbers(numbers: list[int]) -> list:
#
#     def double(num: int) -> int:
#         return num * 2
#
#     def is_odd(num: int) -> bool:
#         return num % 2 != 0
#
#     return [double(num) for num in numbers if is_odd(num)]
#
#
#
# assert(double_odd_numbers([1, 2, 3, 4, 5])) == [2, 6, 10]
# assert(double_odd_numbers([6, 8, 10, 2])) == []
# assert(double_odd_numbers([-43, 91, 932, 9201, 32, 93])) == [-86, 182, 18402, 186]
# print("You are breathtaking!")


# def calculate(x: int, y: int | float, operation: str = 'a') -> None:
#
#     def addition() -> None:
#         print(x + y)
#
#     def subtraction() -> None:
#         print(x - y)
#
#     def division() -> None:
#         if y == 0:
#             print('На ноль делить нельзя!')
#         else:
#             print(x / y)
#
#     def multiplication() -> None:
#         print(x * y)
#
#     match operation:
#         case 'a':
#             addition()
#         case 's':
#             subtraction()
#         case 'd':
#             division()
#         case 'm':
#             multiplication()
#         case _:
#             print('Ошибка. Данной операции не существует')
#
#
# calculate(10, 4, 's')  # == 6
# calculate(10, 0, 'd')  # == 'На ноль делить нельзя!'
# calculate(10, 4, 'w')  # == 'Ошибка. Данной операции не существует'
# calculate(1, 2, 'a')  # == 3
# calculate(3, 1, 'd')  # == 3.0
