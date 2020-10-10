#!/usr/bin/env python3

# Example: nums = [2,3,4,5,6,7], target = 6, output: [0,2]
# as nums[0] + nums[2] = target

def two_sum(nums, target):
    """Returns a list of index of two numbers if the sum of them
    is equal to target number, None otherwise"""
    seen = {}
    for index, num in enumerate(nums):
        another = target - num
        if another in seen:
            return [seen[another], index]
        else:
            seen[num] = index
    return "No such pair in the list"

print(two_sum([2,3,4,5,6,7], 6))
