# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:13:25 2024

@author: FK
"""

# =============================================================================
# Selection sort
# =============================================================================

# 1. Find the minimun value (check the entire list)
# 2. Place the min_val to index 0

l1 = [5, 15, 1, 45, 0, 6]

# For non-duplicate numbers, using min() / max()
def selection_sort1(l1):
    for i in range(len(l1)):
        min_val = min(l1[i:]) # Adcending order. Otherwise use max()
        min_ind = l1.index(min_val) # This index method only returns the first occurance
        l1[i], l1[min_ind] = l1[min_ind], l1[i]# Swap in python
    return l1
selection_sort1(l1)



l2 = [5, 15, 1, 45, 0, 0, 0, 6]
# Works for duplicate numbers as well
# list.index(element, start, end)
def selection_sort2(l1):
    for i in range(len(l1)-1): # Only need to iterate till the last second one
        min_val = min(l1[i:])
        min_ind = l1.index(min_val, i) # This index method only gives the index of one
        if l1[i] != l1[min_ind]: # No need to swap if the same value
            l1[i], l1[min_ind] = l1[min_ind], l1[i]# Swap in python
        print(l1) # Print the iterations
    return l1
selection_sort2(l2)

# Without built-in methods of min() and max()
l3 = [5, 15, 1, 45, 0, 0, 0, 6]
def selection_sort3(l1):
    for i in range(len(l1)-1): # Only need to iterate till the last second one
        min_val = l1[i] # Take the first one of unsorted part as the minimum value first
        for j in range(i+1, len(l1)):
            if l1[j] < min_val:
                min_val = l1[j]
        min_ind = l1.index(min_val, i) # This index method only gives the index of one
        if l1[i] != l1[min_ind]: # No need to swap if the same value
            l1[i], l1[min_ind] = l1[min_ind], l1[i]# Swap in python
        print(l1) # Print the iterations
    return l1
selection_sort3(l3)

# =============================================================================
# Bubble Sort / Sinking sort
# =============================================================================

# 1. Start at index 0, compare
# 2. Swap if needed
# 3. Move forward

l4 = [10, 15, 4, 23, 0]

def bubble_sort(l1):
    for j in range(len(l1)-1):
        for i in range(len(l1)-1-j): # For each iteration, the biggest value will be pushed to the last
            if l1[i] > l1[i+1]:
                l1[i], l1[i+1] = l1[i+1], l1[i]
    return l1
bubble_sort(l4)       



# =============================================================================
# Quick sort
# =============================================================================

# =============================================================================
# Quick sort
# =============================================================================

