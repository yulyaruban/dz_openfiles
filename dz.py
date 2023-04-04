import os

# from pprint import pprint
# with open('recipes.txt', 'rt') as file:
#     cook_book = {}
#     for line in file:
#         dish_name = line.strip()
#         ingridients_count = int(file.readline().strip())
#         ingridients_list = []
#         for _ in range(ingridients_count):
#             ingr_name, quantity, unit = file.readline().strip().split(' | ')
#             ingridients_list.append({
#                 'ingridient' : ingr_name,
#                 'quantity' : quantity,
#                 'unit': unit

#             })
#         file.readline()
#         cook_book[dish_name] = ingridients_list
#     pprint(cook_book)

# def get_shop_list_by_dishes(dishes, person_count):
#     ingr_list = dict()

#     for dish_name in dishes:  # итерируем список полученных блюд
#         if dish_name in cook_book:
#             for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
#                 meas_quan_list = dict()
#                 if ings['ingridient'] not in ingr_list:
#                     meas_quan_list['measure'] = ings['unit']
#                     meas_quan_list['quantity'] = int(ings['quantity']) * person_count
#                     ingr_list[ings['ingridient']] = meas_quan_list
#                 else:
#                     ingr_list[ings['ingridient']]['quantity'] = ingr_list[ings['ingridient']]['quantity'] + \
#                                                                      ings['quantity'] * person_count

#         else:
#             print(f'\n"Такого блюда нет в списке!"\n')
#     return ingr_list

# pprint(get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 3))

def rewrite_file(path1=None, path2=None, path3=None):
    res_file = "rewrite.txt"
    file1_path = os.path.join(os.getcwd(), path1)
    file2_path = os.path.join(os.getcwd(), path2)
    file3_path = os.path.join(os.getcwd(), path3)
    with open(file1_path, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(file2_path, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(file3_path, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open(res_file, 'w', encoding='utf-8') as final:
        if len(file1) < len(file2) and len(file1) < len(file3):
            final.write(path1 + '\n')
            final.write(str(len(file1)) + '\n')
            final.writelines(file1)
            final.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            final.write(path2 + '\n')
            final.write(str(len(file2)) + '\n')
            final.writelines(file2)
            final.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            final.write(path3 + '\n')
            final.write(str(len(file3)) + '\n')
            final.writelines(file3)
            final.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(
                    file3):
            final.write(path1 + '\n')
            final.write(str(len(file1)) + '\n')
            final.writelines(file1)
            final.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(
                    file3):
            final.write(path2 + '\n')
            final.write(str(len(file2)) + '\n')
            final.writelines(file2)
            final.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(
                    file2):
            final.write(path3 + '\n')
            final.write(str(len(file3)) + '\n')
            final.writelines(file3)
            final.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            final.write(path1 + '\n')
            final.write(str(len(file1)) + '\n')
            final.writelines(file1)
            final.write('\n')
        elif len(file2) > len(file1) and len(file2) > len(file3):
            final.write(path2 + '\n')
            final.write(str(len(file2)) + '\n')
            final.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
            final.write(path3 + '\n')
            final.write(str(len(file3)) + '\n')
            final.writelines(file3)
            final.write('\n')
    return

rewrite_file('1.txt', '2.txt', '3.txt')