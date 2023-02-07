# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

list = []
for i in range(int(input('Введите размер списка -> '))):
    list.append(random.randint(1, 100))
print(list)

desired_num = int(input('Введите число для поиска -> '))
count = 0
for i in range(len(list)):
    if list[i] == desired_num:
        count += 1
if count != 0:
    print(f'Искомое значение встречается -> {count} раз')
else:
    close_num = list[0]
    dif = abs(list[0] - desired_num)    
    for i in list:
        if abs(i-desired_num) < dif:
            dif = abs(i-desired_num)
            close_num = i
    print(f'Максимально близкое значение в списке -> {close_num}')
