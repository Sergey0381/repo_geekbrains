# Task 4

my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
new_my_list = [el for el in my_list if my_list.count(el) < 2]
print(new_my_list)