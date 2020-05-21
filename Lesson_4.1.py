#  Task_1

from sys import argv  # Из библиотеки sys импортируем элемент argv для ввода аргументов из cmd

name, time, salary, bonus = argv
try:  # Отлавливаем ошибку
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus  # Производим расчёт ЗП
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
