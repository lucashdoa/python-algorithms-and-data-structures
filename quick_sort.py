unsorted_list = [9, 7, 5, 8, 2, 6, 3, 4, 0, 1]


def quick_sort(list):
    if len(list) <= 1:
        return list
    less_than_pivot = []
    greater_than_pivot = []
    pivot = list[0]
    for index in range(1, len(list)):
        if list[index] > pivot:
            greater_than_pivot.append(list[index])
        else:
            less_than_pivot.append(list[index])
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


print(quick_sort(unsorted_list))
