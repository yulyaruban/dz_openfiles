from pprint import pprint
with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingridients_count = int(file.readline().strip())
        ingridients_list = []
        for _ in range(ingridients_count):
            ingr_name, quantity, unit = file.readline().strip().split(' | ')
            ingridients_list.append({
                'ingridient' : ingr_name,
                'quantity' : quantity,
                'unit': unit

            })
        file.readline()
        cook_book[dish_name] = ingridients_list
    pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    ingr_list = dict()

    for dish_name in dishes:  # итерируем список полученных блюд
        if dish_name in cook_book:
            for ings in cook_book[dish_name]:  # итерируем ингридиенты в блюде
                meas_quan_list = dict()
                if ings['ingridient'] not in ingr_list:
                    meas_quan_list['measure'] = ings['unit']
                    meas_quan_list['quantity'] = int(ings['quantity']) * person_count
                    ingr_list[ings['ingridient']] = meas_quan_list
                else:
                    ingr_list[ings['ingridient']]['quantity'] = ingr_list[ings['ingridient']]['quantity'] + \
                                                                     ings['quantity'] * person_count

        else:
            print(f'\n"Такого блюда нет в списке!"\n')
    return ingr_list

pprint(get_shop_list_by_dishes(['Омлет','Запеченный картофель'], 3))

