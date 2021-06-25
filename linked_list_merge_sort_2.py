from linked_list_2 import LinkedList

l = LinkedList()
l.add(2)
l.add(3)
l.add(4)
l.add(5)
l.add(6)
l.add(7)
l.add(8)


def merge_sort(linked_list):
    """
    Sorts a linked list in ascending order
    """

    # Base Case
    if linked_list.size() <= 1:
        return linked_list

    left_half, right_half = split(linked_list)
    # print("Esquerda")
    # print(left_half)
    # print("Direita")
    # print(right_half)

    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)


def split(linked_list):
    right_half = LinkedList()
    mid_point = linked_list.size() // 2
    index = 0
    current_node = linked_list.head
    while index < mid_point - 1:
        current_node = current_node.next_node
        index += 1
    right_half.add(0)
    right_half.head = current_node.next_node
    current_node.next_node = None
    left_half = linked_list
    return left_half, right_half


def merge(left, right):
    merged_list = LinkedList()
    current_left = left.head
    current_right = right.head

    merged_list.add(0)
    current = merged_list.head

    while current_left or current_right:
        if current_left is None:
            current.next_node = current_right
            current_right = current_right.next_node
        elif current_right is None:
            current.next_node = current_left
            current_left = current_left.next_node
        else:
            if current_right.value < current_left.value:
                current.next_node = current_right
                current_right = current_right.next_node
            else:
                current.next_node = current_left
                current_left = current_left.next_node
        current = current.next_node
    merged_list.head = merged_list.head.next_node
    return merged_list


print(l)
print(merge_sort(l))
