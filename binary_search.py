def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

numbers = [1,2,3,4,5,6,7,8,9,10]

index = binary_search(numbers, 2)

def verify():
    if index:
        print("The number was found on index: ", index)
    else:
        print("The number was not found on the list")

verify()

