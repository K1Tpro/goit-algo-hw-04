def total_salary(path):
    try:
        with open(path, "r") as fh:
            lines = [el.strip().split(',') for el in fh.readlines()]
        total = 0
        for p in lines:
            total += int(p[1])
        average = float('{:.2f}'.format(total / len(lines)))
        return total, average
    except FileNotFoundError:
        print('Файл пошкоджено або він не існує')


total, average = total_salary("text.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
