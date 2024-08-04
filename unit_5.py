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
