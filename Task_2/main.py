def get_cats_info(path):
    try:
        with open(path, "r") as fh:
            lines = [el.strip().split(',') for el in fh.readlines()]
        cats = []
        for cat in lines:
            id, name, age = cat
            cat_info = {
                'id': id,
                'name': name,
                'age': int(age)
            }
            cats.append(cat_info)
        return cats

    except FileNotFoundError:
        print('Файл пошкоджено або він не існує')


print(get_cats_info('text.txt'))

