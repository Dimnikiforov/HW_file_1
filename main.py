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
# pprint(cook_book)
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
# print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 1))

with open('1.txt', encoding='utf-8') as file:
    txt_1 = file.readlines()
    len_txt_1 = len(txt_1)
with open('2.txt', encoding='utf-8') as file:
    txt_2 = file.readlines()
    len_txt_2 = len(txt_2)
with open('3.txt', encoding='utf-8') as file:
    txt_3 = file.readlines()
    len_txt_3 = len(txt_3)
if len_txt_1 < len_txt_2 < len_txt_3:
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write('1.txt\n')
        file.write(str(len_txt_1) + '\n')
        file.writelines(txt_1)
elif len_txt_2 < len_txt_1 < len_txt_3:
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write('2.txt\n')
        file.write(str(len_txt_2) + '\n')
        file.writelines(txt_2)
else:
    with open('result.txt', 'w', encoding='utf-8') as file:
        file.write('3.txt\n')
        file.write(str(len_txt_3) + '\n')
        file.writelines(txt_3)
if len_txt_2 < len_txt_1 < len_txt_3 or len_txt_3 < len_txt_1 < len_txt_2:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('1.txt\n')
        file.write(str(len_txt_1) + '\n')
        file.writelines(txt_1)
elif len_txt_1 < len_txt_2 < len_txt_3 or len_txt_3 < len_txt_1 < len_txt_1:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('2.txt\n')
        file.write(str(len_txt_2) + '\n')
        file.writelines(txt_2)
else:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('3.txt\n')
        file.write(str(len_txt_3) + '\n')
        file.writelines(txt_3)
if len_txt_1 > len_txt_2 > len_txt_3:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('1.txt\n')
        file.write(str(len_txt_1) + '\n')
        file.writelines(txt_1)
elif len_txt_2 > len_txt_1 > len_txt_3:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('2.txt\n')
        file.write(str(len_txt_2) + '\n')
        file.writelines(txt_2)
else:
    with open('result.txt', 'a', encoding='utf-8') as file:
        file.write('3.txt\n')
        file.write(str(len_txt_3) + '\n')
        file.writelines(txt_3)

