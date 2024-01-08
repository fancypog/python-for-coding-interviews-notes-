# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:22:20 2024

@author: FK
"""
# =============================================================================
# Binary search
# =============================================================================
l1 = [1, 23, 0, 18, 3, 5, 34, 8]

def binarySearch(nums, target, l, r):
    m = (l + r)//2
    if l <= r:
        if nums[m] > target:
            return binarySearch(nums, target, l, m-1)
        elif nums[m] < target:
            return binarySearch(nums, target, m+1, r)
        elif nums[m] == target:
            return m
        else:
            return - 1
    else:
        return -1
    return binarySearch(nums, target, 0, len(nums) - 1)

binarySearch(l1, 5, 0, len(l1))
