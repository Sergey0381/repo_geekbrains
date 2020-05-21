# Task 2

from itertools import groupby
my_list = [200, 2, 12, 73, 1, 1, 4, 10, 7, 1, 78, 123, 55, 2]
my_list.sort()
new_list = [i for i,_ in groupby(my_list)]
print(new_list)