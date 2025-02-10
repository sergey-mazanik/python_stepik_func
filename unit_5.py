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
from itertools import count
from sys import flags


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


# def apply(func, obj):
#     return [func(i) for i in obj]
#
#
# def repeater(value, n=5):
#     return str(value) * n
#
#
# print(apply(repeater, 'hello'))


# def compute(lst: list, *args):
#     new_lst = []
#     for func in lst:
#         for elem in args:
#             new_lst.append(func(elem))
#     return new_lst
#
#
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# def repeater(value, n=10):
#     return str(value) * n
#
# def square(num):
#     return num ** 2
#
# print(compute([repeater, dec, inc, square], 5, 7, 0, True))


# def compute(lst: list, *args):
#     new_lst = []
#     for elem in args:
#         for func in lst:
#             elem = func(elem)
#         new_lst.append(elem)
#     return new_lst
#
#
# def inc(num):
#     return num + 1
#
# def dec(num):
#     return num - 1
#
# def repeater(value, n=3):
#     return str(value) * n
#
# def square(num):
#     return num ** 2
#
# print(compute([dec, inc, square, repeater], 5, 7, 0, True))


# def filter_list(f: callable, lst: list[...]) -> list:
#     return [i for i in lst if f(i)]
#
#
# def is_positive(num):
#     return num > 0
#
# numbers = [-1, 2, -3, 4, 5, -6, 7, -8, -9, 10]
# positive_numbers = filter_list(is_positive, numbers) # берем только положительные
# print(positive_numbers)


# def filter_collection(f, obj):
#     if isinstance(obj, list):
#         return [i for i in obj if f(i)]
#     elif isinstance(obj, tuple):
#         return tuple([i for i in obj if f(i)])
#     elif isinstance(obj, str):
#         new_str = ''
#         for i in obj:
#             if f(i):
#                 new_str += i
#         return new_str
#
#
# print(filter_collection(lambda x: x not in 'aeiou', 'I never heard those lyrics before'))


# def aggregation(func, sequence):
#     lst = [func(sequence[0], sequence[1])]
#     for i in sequence[2:]:
#         lst.append(func(i, lst[-1]))
#     return lst
#
# def get_min(x, y):
#     return min(x, y)
#
# # агрегируем нахождение минимума
# print(aggregation(get_min, [9, 6, 7, 8, 5, 1, 2, 4]))


# def aggregation(func, sequence):
#     lst = [func(sequence[0], sequence[1])]
#     temp = func(sequence[0], sequence[1])
#     for i in sequence[2:]:
#         temp = func(i, lst[-1])
#         lst.append(func(i, lst[-1]))
#     return temp
#
# def get_add(x, y):
#     return x + y
#
# print(aggregation(get_add, [11, 4, 5, 7, 8, 10]))


# def aggregation(func, sequence, initial = None):
#     if initial:
#         lst = [initial]
#         temp = initial
#         for i in sequence:
#             temp = func(i, lst[-1])
#             lst.append(func(i, lst[-1]))
#         return temp
#     else:
#         lst = [func(sequence[0], sequence[1])]
#         temp = func(sequence[0], sequence[1])
#         for i in sequence[2:]:
#             temp = func(i, lst[-1])
#             lst.append(func(i, lst[-1]))
#         return temp
#
# print(aggregation(lambda x, y: x * y, [2, 5, 10, 1, 2], initial=50))


# def multiply(a: int) -> callable:
#     def inner(b: int) -> int:
#         return b * a
#     return inner
#
#
#
# f_2 = multiply(2)
# print("Умножение 2 на 5 =", f_2(5)) #10
# print("Умножение 2 на 15 =", f_2(15)) #30
# f_3 = multiply(3)
# print("Умножение 3 на 5 =", f_3(5)) #15
# print("Умножение 3 на 15 =", f_3(15)) #45


# def make_repeater(num: int) -> callable:
#     def inner(el: str) -> str:
#         return num * el
#     return inner
#
#
# repeat_5 = make_repeater(5)
# print(repeat_5('Hello'))
# print(repeat_5('World'))
#
# repeat_2 = make_repeater(2)
# print(repeat_2('Pizza'))
# print(repeat_2('Pasta'))


# def create_accumulator() -> callable:
#     count = 0
#     def inner(num: int | float) -> int | float:
#         nonlocal count
#         count += num
#         return count
#     return inner
#
#
# closure = create_accumulator()
#
# print(closure(4))
# print(closure(400))
# print(closure(4.5))
# print(closure(0.5))
#
# closure_2 = create_accumulator()
#
# print(closure_2(0))
# print(closure_2(1))
# print(closure_2(3))
# print(closure_2(7))


# def create_accumulator(a: int | float = 0) -> callable:
#     count = a
#     def inner(num: int | float) -> int | float:
#         nonlocal count
#         count += num
#         return count
#     return inner
#
#
# closure = create_accumulator(300)
#
# print(closure(4))
# print(closure(400))
# print(closure(4.5))
# print(closure(0.5))
#
# closure_2 = create_accumulator()
#
# print(closure_2(0))
# print(closure_2(1))
# print(closure_2(3))
# print(closure_2(7))


# def countdown(num: int) -> callable:
#     count = num
#     def inner() -> int | float | None:
#         nonlocal count
#         if count == 0:
#             print(f'Превышен лимит, вы вызвали более {num} раз')
#         else:
#             print(count)
#             count -= 1
#             return count
#     return inner
#
#
# a = countdown(2)
# b = countdown(2)
# a()
# b()
# b()
# b()
# a()
# a()


# def count_calls():
#     total_calls = 0
#     def inner():
#         nonlocal total_calls
#         total_calls += 1
#         inner.total_calls = total_calls
#         return total_calls
#     inner.total_calls = total_calls
#     return inner
#
#
#
# counter1 = count_calls()
# counter2 = count_calls()
# counter1()
# print(counter1.total_calls, counter2.total_calls)
# counter1()
# counter2()
# print(counter1.total_calls, counter2.total_calls)
# counter2()
# counter2()
# print(counter1.total_calls, counter2.total_calls)


# def create_dict():
#     my_dict = {}
#     count = 0
#     def add_to_dict(el: any):
#         nonlocal count
#         count += 1
#         my_dict[count] = el
#         return my_dict
#     return add_to_dict
#
#
# f_1 = create_dict()
# print(f_1('privet'))
# print(f_1('poka'))
# print(f_1([5, 2, 3]))
#
# f2 = create_dict()
# print(f2(5))
# print(f2(15))


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print('---Start calculation---')
#         result = func(*args, **kwargs)
#         print(f'---Finish calculation. Result is {result}---')
#         return result
#     return wrapper
#
#
# # @decorator
# # def add(a, b):
# #     return a + b
#
#
# @decorator
# def concatenate(**kwargs):
#     result = ""
#     for arg in kwargs.values():
#         result += str(arg)
#     return result
#
#
# concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!")


# def repeater(func):
#     def wrapper(*args, **kwargs):
#         for i in range(3):
#             func(*args, **kwargs)
#         return func
#     return wrapper
#
#
# @repeater
# def some_func(a, b, c):
#     print(a ** b + c)
#
#
# some_func(4, 5, 4)
# some_func(14, 51, 34)


# def double_it(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper
#
#
# @double_it
# def get_sum_kwargs_values(**kwargs):
#     return sum(kwargs.values())
#
#
# print(get_sum_kwargs_values(a=4, b=5, c=7))
# print(get_sum_kwargs_values(a=4, b=5, d=3, t=6, r=8))


# def uppercase_elements(func):
#     def wrapper(*args, **kwargs):
#         temp = func(*args, **kwargs)
#         if isinstance(temp, dict):
#             return {(k.upper() if isinstance(k, str) else k): v for k, v in temp.items()}
#         elif isinstance(temp, list):
#             return [i.upper() if isinstance(i, str) else i for i in temp]
#     return wrapper
#
#
# @uppercase_elements
# def my_func(**kwargs):
#     return {1: 'one', 2: 'store', 'three': 3, 'four': 4} | kwargs
#
# print(my_func(**{'Five': 5, 'sIx': 6}))


# def first_validator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f"Начинаем важную проверку")
#         if len(args) == 3:
#             func(*args, **kwargs)
#         else:
#             print(f"Важная проверка не пройдена")
#             return None
#         print(f"Заканчиваем важную проверку")
#
#     return my_wrapper
#
#
# def second_validator(func):
#     def my_wrapper(*args, **kwargs):
#         print(f"Начинаем самую важную проверку")
#         if kwargs.get('name') == 'Boris':
#             func(*args)
#         else:
#             print(f"Самая важная проверка не пройдена")
#             return None
#         print(f"Заканчиваем самую важную проверку")
#
#     return my_wrapper
#
#
# # используйте декораторы
# @second_validator
# @first_validator
# def sum_values(*args):
#     print(f'Получили результат равный {sum(args)}')
#
#
# # вызовите функцию sum_values()
# sum_values(33, 33, 11, name='Boris')


# def validate_all_args_str(func):
#     def wrapper(*args, **kwargs):
#         flag = False
#         for arg in args:
#             if not isinstance(arg, str):
#                 print('Все аргументы должны быть строками')
#                 flag = True
#         if not flag:
#             new = func(*args, **kwargs)
#             return new
#     return wrapper
#
#
#
# @validate_all_args_str
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
#
# print(concatenate("Через", 9, "Месяцев"))


# def validate_all_kwargs_int_pos(func):
#     def wrapper(*args, **kwargs):
#         flag = False
#         for kwarg in kwargs.values():
#             if not isinstance(kwarg, int) or kwarg <= 0:
#                 print('Все именованные аргументы должны быть положительными числами')
#                 flag = True
#                 break
#         if not flag:
#             new = func(*args, **kwargs)
#             return new
#     return wrapper
#
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a="i", b='Love', c="Python"))
#
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate(a=10, b=20, c=50))
#
# @validate_all_args_str
# @validate_all_kwargs_int_pos
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
# print(concatenate('Hello', 2, 'World', a="i", b='Love', c="Python"))


# def filter_even(func):
#     def wrapper(*args, **kwargs):
#         lst = [
#             arg for arg in args if
#             (
#                     (isinstance(arg, int) and arg % 2 == 0) or
#                     (arg is False) or
#                     (isinstance(arg, (tuple, str, list, dict)) and len(arg) % 2 == 0)
#             )
#         ]
#         return func(*lst, **kwargs)
#     return wrapper
#
#
# def delete_short(func):
#     def wrapper(*args, **kwargs):
#         new_dict = {k: v for k, v in kwargs.items() if len(k) >= 5}
#         return func(*args, **new_dict)
#     return wrapper
#
#
# @filter_even
# def concatenate(*args):
#     result = ""
#     for arg in args:
#         result += arg
#     return result
#
# print(concatenate("Ну", "Когда", "Уже", "Я", "Выучу", "Питон?"))
# print()
#
# @delete_short
# def info_kwargs(**kwargs):
#     """Выводит информацию о переданных kwargs"""
#     for k, v in sorted(kwargs.items()):
#         print(f'{k} = {v}')
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# print()
#
# @filter_even
# @delete_short
# def concatenate(*args, **kwargs):
#     result = ""
#     for arg in args + tuple(kwargs.values()):
#         result += str(arg)
#     return result
#
#
# print(concatenate([1], [1, 2], {1:1, 2:2}, {1:1}, a="За", qwer=10, ccccc="Месяцев"))
