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


# def words_length(words: list):
#     for i in range(len(words)):
#         words[i] = len(words[i])


# def my_func(collection, n):
#     new_collection = collection.copy()
#     for i in range(1, n + 1):
#         new_collection.append(i)
#     return new_collection


# def print_values(*args):
#     for i in args:
#         print(*i, end=' ')


# def count_args(*args):
#     return len(args)


# def multiply(*args):
#     res = 1
#     for i in args:
#         res *= i
#     return res


# def check_sum(*args):
#     print('not enough' if sum(args) < 50 else 'verification passed')


# def is_only_one_positive(*args) -> bool:
#     return len(list(filter(lambda x: x > 0, args))) == 1


# def print_goods(*args):
#     lst = []
#     for i in args:
#         if isinstance(i, str) and i:
#             lst.append(i)
#     if lst:
#         for n, i in enumerate(lst, 1):
#             print(f'{n}. {i}')
#     else:
#         print('Нет товаров')


# def print_args(a, b, c, d):
#     print(a, b, c, d)
#
#
# dct = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
# print_args(**dct)


# def concatenate(**kwargs):
#     return ''.join([str(v) for v in kwargs.values()])
#
#
# print(concatenate(a="Я", b="Выучу", c="Этот", d="Питон", e="!"))
# print(concatenate(first='i got ', second=5, third=" stars"))
# print(concatenate(t='Happy', y="Meal", w="Cost", m=10, b='Buks'))
# print(concatenate(q='iHave', w="next", e="Coins", r=[10, 5, 10, 7]))


# def create_actor(**kwargs):
#     base_dict = {
#             'name': 'Райан',
#             'surname': 'Рейнольдс',
#             'age': 47,
#             }
#     if not kwargs:
#         return base_dict
#     return {**base_dict, **kwargs}
#
#
# actor = create_actor(surname='Уиллис', age=69, name='Брюс')
# print(actor)


# def info_kwargs(**kwargs):
#     print(*sorted([f'{k} = {v}' for k, v in kwargs.items()]), sep='\n')
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)
# info_kwargs(c=43, b= 32, a=32)
# info_kwargs(b=3,c=2,a=1)
# info_kwargs(cool='hello')


# def print_scores(name, *args):
#     print(f'Student name: {name}')
#     print(*sorted(args), sep='\n')
#
#
# print_scores("Jud", 100, 95, 88, 92, 99)


# def truncate_sentences(num, *args):
#     lst = [i[:num] for i in args]
#     print(*lst, sep='\n')
#
#
# truncate_sentences(
#     5,
#     "Мой дядя самых честных правил,",
#     "Когда не в шутку занемог,",
#     "Он уважать себя заставил",
#     "И лучше выдумать не мог.",
#     "Его пример другим наука;",
#     "Но, боже мой, какая скука",
#     "С больным сидеть и день и ночь,",
#     "Не отходя ни шагу прочь!",
# )


# def make_strings_big(*args, reverse=False):
#     if reverse:
#         print(*[arg.lower() for arg in args], sep='\n')
#     else:
#         print(*[arg.upper() for arg in args], sep='\n')
#
#
# make_strings_big('У лукоморья дуб зелёный',
#                  'Златая цепь на дубе том:',
#                  'И днём и ночью кот учёный')
