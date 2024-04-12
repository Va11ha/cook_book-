def Person(cook_book, dishes, person_count):
    shopping_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']
                if ingredient_name not in shopping_list:
                    shopping_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
                else:
                    shopping_list[ingredient_name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' отсутствует в книге рецептов!")

    return shopping_list

# Пример использования
cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

dishes = ['Омлет', 'Утка по-пекински', 'Салат']  # 'Салат' отсутствует в книге рецептов
person_count = 2

shopping_list = Person(cook_book, dishes, person_count)

for ingredient, info in shopping_list.items():
    print(f"{ingredient}: {info['quantity']} {info['measure']}")
