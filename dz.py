from pprint import pprint
with open('recipes.txt', 'rt') as file:
    dishes = {}
    for line in file:
        dish_name = line.strip()
        ingridients_count = int(file.readline().strip())
        ingridients = []
        for _ in range(ingridients_count):
            ingridient, quantity, unit = file.readline().strip().split(' | ')
            ingridients.append({
                'ingridient' : ingridient,
                'quantity' : quantity,
                'unit': unit

            })
        file.readline()
        dishes[dish_name] = ingridients
    pprint(dishes)