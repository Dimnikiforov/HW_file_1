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