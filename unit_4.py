# from typing import Optional, List
#
#
# def get_first_repeated_word(words: List[str]) -> Optional[str]:
#     """Находит первый дубль в списке"""
#     temp = []
#     for word in words:
#         if word not in temp:
#             temp.append(word)
#         else:
#             return word
#
#
# print(get_first_repeated_word(['ab', 'ca', 'bc', 'Ab', 'cA', 'aB', 'bc']))


# def rotate(lst: list[int | float], shift: int = 1) -> [int | float]:
#     """Функция выполняет циклический сдвиг списка на shift позиций вправо(shift>0) или влево(shift<0)"""
#     if not lst:
#         return lst
#     return lst[-shift % len(lst):] + lst[:-shift % len(lst)]
#
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate([1, 2, 3, 4, 5, 6, 7], -3))


# def rotate(tpl: tuple[int | float, ...], shift: int = 1) -> tuple[int | float, ...]:
#     """Функция выполняет циклический сдвиг кортежа на shift позиций вправо(shift>0) или влево(shift<0)"""
#     if not tpl:
#         return tpl
#     return tpl[-shift % len(tpl):] + tpl[:-shift % len(tpl)]
#
#
# print(rotate.__doc__)
# print(rotate.__annotations__)
# print(rotate((1, 2, 3, 4, 5, 6, 7), -3))


# def rotate_letter(letter: str, shift: int) -> str:
#     """Функция сдвигает символ letter на shift позиций"""
#     new_letter: str | None = chr(((ord(letter) - ord('a') + shift) % 26) + 97)
#     return new_letter
#
#
# def caesar_cipher(phrase: str, key: int) -> str:
#     """Шифр Цезаря"""
#     rez: str | None = ''
#     for i in phrase:
#         if i.isalpha():
#             rez += rotate_letter(i, key)
#         else:
#             rez += ' '
#     return rez
#
#
# print(caesar_cipher('lost in the echo', -120))
