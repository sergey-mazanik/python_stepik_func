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


# def words_length(lst: list) -> list:
#     return [len(i) for i in lst]
#
#
# print(words_length(['Hello', 'world!']))
# print(words_length(['Python', 'is', 'awesome!']))
# print(words_length(['You', 'should', 'learn', 'it!']))


# def filter_long_words(words: list, num: int) -> list:
#     return [word for word in words if len(word) > num]
#
#
# print(filter_long_words(['sister', 'arena', 'formal', 'arena', 'spill'], 5))
# print(filter_long_words(['Python', 'stole', 'my', 'heart'], 4))
# print(filter_long_words(['ex', 'care', 'room', 'law'], 3))


# def is_member(value: str, lst: list) -> bool:
#     return value in lst
#
#
# print(is_member("e", ['a', 'e', 'i', 'o', 'u']))


# def overlapping(lst1: list, lst2: list) -> bool:
#     flag = False
#     for i in lst1:
#         if is_member(i, lst2):
#             flag = True
#             break
#     return flag
#
#
# print(overlapping(['nope', 'nothing', 'in'], ['common']))
# print(overlapping(['this', 'might', 'work'], ['or', 'maybe', 'this']))
# print(overlapping(['I', 'think', 'I am', 19], ['19', 'bananas']))


# def find_longest_word_len(words: list) -> int:
#     return len(max(words, key=len))
#
#
# print(find_longest_word_len(['hello', 'world', 'Python', 'reserve']))
# print(find_longest_word_len(['default', 'ghostwriter', 'bother', 'applaud', 'skate', 'way']))
# print(find_longest_word_len(['brain', 'candle', 'rare', 'shy']))


# def register_check(people_dict: dict):
#     register_people = {key: value for (key, value) in people_dict.items() if value == 'yes'}
#     return len(register_people)
#
#
# people = {'Igor': 'yes', 'Stas': 'no', 'Peter': 'no', 'Mary': 'yes'}
# print(register_check(people))
# people = {'Igor': 'no', 'Vasya': 'no', 'Peter': 'no', 'Mary': 'no'}
# print(register_check(people))
# people = {'Igor': 'yes', 'Vasya': 'yes', 'Peter': 'yes',
#           'Mary': 'no', 'Alex': 'yes', 'Marina': 'yes'}
# print(register_check(people))


# def create_tuples(lst1: list, lst2: list) -> list:
#     return list(zip(lst1, lst2))
#
#
# print(create_tuples([1, 2, 3, 4], [5, 6, 7, 8]))
