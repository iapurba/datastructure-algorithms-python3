#!/usr/bin/env python3
array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

# print(sorted(array1 + array2)

def mergeSortedArray(array1, array2):
    merged_array = []
    if len(array1) == 0:
        return array2
    if len(array2) == 0:
        return array1

    i = 0
    j = 0
    while i < len(array1):
        arra1Item = array1[i]
        array2Item = array2[j]
        print(arra1Item, array2Item)
        if (arra1Item < array2Item):
            merged_array.append(arra1Item)
            arra1Item = array1[i]
            i += 1
        else:
            merged_array.append(array2Item)
            array2Item = array2[j]
            j += 1
    print(merged_array)
    return merged_array

mergeSortedArray(array1, array2)
