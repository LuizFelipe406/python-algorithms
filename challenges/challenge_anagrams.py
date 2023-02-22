# Ref: Course
def merge_sort(string, start=0, end=None):
    if end is None:
        end = len(string)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(string, start, mid)
        merge_sort(string, mid, end)
        merge(string, start, mid, end)


def merge(string, start, mid, end):
    left = string[start:mid]
    right = string[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            string[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            string[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            string[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            string[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    first_string_in_list = [letter.lower() for letter in first_string]
    second_string_in_list = [letter.lower() for letter in second_string]

    merge_sort(first_string_in_list)
    merge_sort(second_string_in_list)

    first_ordered_string = "".join(first_string_in_list)
    second_ordered_string = "".join(second_string_in_list)
    is_anagram_result = True

    if len(first_string) <= 0 or len(second_string) <= 0:
        return (first_ordered_string, second_ordered_string, False)

    for letter in first_ordered_string:
        if letter != second_ordered_string[first_ordered_string.index(letter)]:
            is_anagram_result = False
            break
    return (first_ordered_string, second_ordered_string, is_anagram_result)
