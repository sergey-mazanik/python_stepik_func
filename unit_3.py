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


# alpha = 'abcdefghijklmnopqrstuvwxyz'
#
#
# def is_pangram(my_str: str):
#     new_str = my_str.lower()
#     s = ''
#     for i in new_str:
#         if i in alpha and i not in s:
#             s += i
#     s = ''.join(sorted(s))
#     return s == alpha
#
#
# print(is_pangram("The quick brown fox jumps over the lazy dog."))
# print(is_pangram("Obviously not a pangram"))
# print(is_pangram("How quickly daft jumping zebras vex!"))


# def translate_to_robber_lang(my_str: str) -> str:
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     new_str = ''
#     for i in my_str:
#         if i.lower() not in vowels and i.isalpha():
#             new_str += f'{i}o{i}'
#         else:
#             new_str += i
#     return new_str
#
#
# print(translate_to_robber_lang("This is kinda fun"))
# print(translate_to_robber_lang("I Think YoU Might BE righT!"))

# def is_table_free(table_number: int) -> bool:
#     return bool(not tables[table_number])
#
#
# def get_free_tables():
#     free_tables = [key for key, value in tables.items() if not value]
#     return free_tables


# def reserve_table(table_number: int, client_name: str) -> None:
#     if is_table_free(table_number):
#         tables[table_number] = client_name
#
#
# def delete_reservation(table_number: int) -> None:
#     tables[table_number] = None


# def reserve_table(table_number: int, client_name: str, client_status: bool) -> None:
#     if is_table_free(table_number):
#         tables[table_number] = {'name': client_name, 'is_vip': client_status}


# def product(my_list: list, start: int = 1) -> int:
#     for i in my_list:
#         start *= i
#     return start
#
#
# print(product([1, 2, 3]))
# print(product([1, 2, 3], start=10))


# shopping_list = {}
#
#
# def add_item(product_name: str, count: int = 1):
#     if shopping_list.get(product_name) is None:
#         shopping_list.setdefault(product_name, count)
#     else:
#         shopping_list[product_name] = shopping_list[product_name] + count


# def show_list(include_quantities: bool = True):
#     if include_quantities:
#         for k, v in shopping_list.items():
#             print(f'{v}x{k}')
#     else:
#         for k, v in shopping_list.items():
#             print(k)


# def create_student(name, age, marks=None):
#     if marks is not None:
#         marks = marks
#     else:
#         marks = []
#     return {
#         'name': name,
#         'age': age,
#         'marks': marks  # оценки
#     }
#
#
# def add_mark(student, mark):
#     student['marks'].append(mark)


# def calculate_per_person(bill: float, count: int, tip_percent: int = 10):
#     tip = bill / 100 * tip_percent
#     return round((bill + tip) / count, 2)
#
#
# print(calculate_per_person(100.0, 5, 0))
# print(calculate_per_person(200.0, 4))
# print(calculate_per_person(200.0, 4, 50))


# def is_table_free(table_number: int) -> bool:
#     return bool(not tables[table_number])
#
#
# def delete_reservation(table_number: int) -> None:
#     tables[table_number] = None
#
#
# def reserve_table(table_number: int, client_name: str, client_status: bool = False) -> None:
#     if is_table_free(table_number):
#         tables[table_number] = {'name': client_name, 'is_vip': client_status}
#
#
# tables = {
#     1: {'name': 'Andrey', 'is_vip': True},
#     2: None,
#     3: None,
#     4: None,
#     5: None,
#     6: None,
#     7: None,
#     8: None,
#     9: {'name': 'Misha', 'is_vip': False},
# }
# print(tables)
# reserve_table(2, 'Niko', True)
# reserve_table(6, 'Chubaka') # не передается вип-статус
# print(tables)
