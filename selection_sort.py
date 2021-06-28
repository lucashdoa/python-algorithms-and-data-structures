unsorted_list = [9, 7, 5, 8, 2, 6, 3, 4, 0, 1]


def selection_sort(list):
    sorted_list = []
    min_index = 0
    while list:
        current_min = list[0]
        min_index = 0
        if len(list) > 1:
            last_index = len(list)
            for index in range(1, last_index):
                if list[index] < current_min:
                    current_min = list[index]
                    min_index = index
        list.pop(min_index)
        sorted_list.append(current_min)
    return sorted_list


print(selection_sort(unsorted_list))
