import random

unsorted_list = [8, 9, 5, 3, 5, 2, 0, 1, 6, 9, 4]

def bogo_sort(list):
    counter = 0
    while not is_sorted(list):
        counter += 1
        print(counter)
        random.shuffle(list)
    return list

def is_sorted(list):
    for index in range(len(list) - 1):
        if list[index] > list[index + 1]:        
            return False
    return True

sorted_list = bogo_sort(unsorted_list)
print(sorted_list)
