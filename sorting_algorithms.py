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

# Divede and conquer
# Pivot element, smaller ones one one side, bigger ones the other

l5 = [14, 100, 25, 1, 14, 17]

# Choose the first/last/median of three element as the pivot element

# To get the correct position of the pivot element

def pivot_place(l1, first, last):
    pivot = l1[first] # Select the first element as the pivot element
    left = first + 1
    right = last # If take the first element as pivot, swop with the right
    # If the last, the left
    while True:
        while left <= right and l1[left] <= pivot:
            left += 1
        while left <= right and l1[right] >= pivot:
            right -= 1
        if right < left:
            break
        else:
            l1[left], l1[right] = l1[right], l1[left]
    l1[first], l1[right] = l1[right], l1[first]
    return right
        


 # Divide the list and do it recursively   
def quick_sort(l1, first, last):
    if first < last:
        p = pivot_place(l1, first, last)
        quick_sort(l1, first, p-1)
        quick_sort(l1, p+1, last)


quick_sort(l5, 0, len(l5)-1)
print(l5)

# =============================================================================
# Merge sort
# =============================================================================

l6 = [14, 36, 2, 0, 25, 61, 0, 5]

def sortArray(nums):
    def merge(nums, L, M, R):
        left, right = nums[L: M+1], nums[M+1: R+1]
        i, j, k = L, 0, 0

        while j < len(left) and k < len(right):
            if left[j] <= right[k]:
                nums[i] = left[j]
                j += 1
            else:
                nums[i] = right[k]
                k += 1
            i += 1
        while j < len(left):
            nums[i] = left[j]
            j += 1
            i += 1
        while k < len(right):
            nums[i] =right[k]
            k += 1
            i += 1

        
    def mergeSort(nums, left, right):
        if left == right:
            return nums
        m = (left + right) // 2
        mergeSort(nums, left, m)
        mergeSort(nums, m+1, right)
        merge(nums, left, m, right)
        return nums
    return mergeSort(nums, 0, len(nums)-1)

sortArray(l6)


