def create_cook_book(file_name):
    cook_book = {}
    with open (file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        ingredient_count = int(lines[i+1].strip())
        i += 2
        
        ingredients = []
        for _ in range(ingredient_count):
            ingredient_info = lines[i].strip().split(' | ')
            ingredient = {
                'ingredient_name': ingredient_info[0],
                'quantity': int(ingredient_info[1]),
                'measure': ingredient_info[2]
            }
            ingredients.append(ingredient)
            i += 1
        
        cook_book[dish_name] = ingredients
        i += 1
    
    return cook_book

file_name = 'recipes.txt'
cook_book = create_cook_book(file_name)
print(cook_book)
