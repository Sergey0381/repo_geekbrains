# Task 3

print(f'Числа от 20 до 240 кратные 20 или 21 -/n'  # как в условии
 f'{[el for el in range(20, 241) if el % 20 == 0 or el  % 21 == 0]}')
print(f'Числа от 20 до 240 кратные 20 или 21 -/n' # более компактный вывод с шагом
      f'{[el for el in range(20,241,20) if el % 20 == 0 or el % 21 == 0]}')