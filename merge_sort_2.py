def merge_sort(unordered_list):
  list_size = len(unordered_list)
  left_list = unordered_list[:list_size//2]
  right_list = unordered_list[list_size//2:]

  if len(unordered_list) <= 1:
    return unordered_list

  left_index = 0
  right_index = 0
  sorted_list = []

  while left_index < len(left_list) and right_index < len(right_list):
    if left_list[left_index] < right_list[right_index]:
      sorted_list.append(left_list[left_index])
      left_index += 1
    elif right_list[right_index] < left_list[left_index]:
      sorted_list.append(right_list[right_index])
      right_index += 1

  print(merge_sort(left_list))
  print(right_list)
  print(sorted_list)
  return sorted_list

 


merge_sort([1, 31, 22, 54, 34, 90, 12, 2, 10])
