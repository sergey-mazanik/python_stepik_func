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
