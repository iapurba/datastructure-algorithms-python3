#!/usr/bin/env python3

# merge subroutine
def merge(left, right):
    """merges two sorted array and returns the merged array as another sorted array"""
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result + right[right_index:] + left[left_index:]


def merge_sort(array):
    """splits and merges by calling merge() function"""
    length = len(array)
    if length == 1:
        return array

    middle = length // 2
    left = array[0:middle]
    right = array[middle:]
    # calling itself recursively until reach to the base case
    # the base case here is an array with length of 1
    return merge(merge_sort(left),merge_sort(right))


array = [9,8,7,6,5,4,3,2,1,50]
print(merge_sort(array))
