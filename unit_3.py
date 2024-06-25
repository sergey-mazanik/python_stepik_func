# def is_adult(age):
#     return age > 17
#
#
# a = int(input())
# if is_adult(a):
#     print('Ух какой большой')
# else:
#     print('Подрасти еще, сынок')


# def is_leap(year: int) -> bool:
#     return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


# def is_palindrome(my_str: str) -> bool:
#     new_str = my_str.lower().replace(' ', '')
#     return new_str == new_str[::-1]


#
# def count_leap_years(y1: int, y2: int) -> int:
#     return len([year for year in range(y1, y2) if is_leap(year)])


# def get_leap_years(y1: int, y2: int) -> list:
#     return [year for year in range(y1, y2) if is_leap(year)]


# def create_palindrome(my_str: str) -> str:
#     new_str = my_str.lower()
#     if new_str == new_str[::-1]:
#         return new_str
#     return f'{new_str}_i_{new_str[::-1]}'


# def is_strings_equal(s1: str, s2: str) -> bool:
#     return sorted(s1) == sorted(s2)
