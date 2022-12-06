with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[dish] = ingredients
from pprint import pprint
pprint(cook_book)
def get_shop_list_by_dishes(dishes, person):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for j in cook_book[dish]:
                if j['ingredient_name'] not in total:
                    total[j['ingredient_name']] = {'measure': j['measure'],
                                                   'quantity': (int(j[('quantity')]) * person)}
                else:
                    total[j['ingredient_name']]['quantity'] += int(j['quantity']) * person
    return total
print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))

