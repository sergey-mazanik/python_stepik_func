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