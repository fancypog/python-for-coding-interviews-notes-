# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:41:33 2023

@author: FK
"""
# =============================================================================
# 1. Variables
# =============================================================================
# Variables in python are dynmically declared
# When you declare a variable, you don't need to declare a type
n = 0
print("n =", n)
# Type is determined at runtime, you can reasign the variable to another type
n = "abc" # reassign as a string
print("n = ", n)

# Multiple assignments
n, m, z= 0, 'abc', False

# Increment: you cannot do ++
n = n + 1
n += 1
n ++ # not working

# None can be reassigned to a value
n = 4
n = None

# =============================================================================
# 2. If statements and for loop
# =============================================================================
# Parentheses are needed for multi-line conditions
if ((n > 2 and n < 5) or n == m):
    n += 1
    
# loop using range()
# Non-inclusive last index: the second argument of the range() function is not included in the loop
# range(n) starts from 0 to n-1 
for i in range(5):
    print(i)
# range (n, m) starts from n to m-1
for i in range(2, 5):
    print(i)
    
# to loop in reverse order, specify a -1 step
for i in range(5, 1, -1):
    print(i)

# =============================================================================
# 3. Simple calculations, the math library
# =============================================================================
# Division is not automatically rounded
print(5 / 2)   # 2.5
# Double slash rounds down
print(5 // 2)   # 2
# For integer division, python always rounds DOWN instead of towards zero
print(-5 // 2)   # -3 instead of -2

# Extra maths methods
import math
# negative modulo: modulo with a minus sign
print(math.fmod(-10, 3))
# floor: round down
print(math.floor(3 / 2))
# ceil: round up
print(math.ceil(3 / 2))
# square root
print(math.sqrt(2))
# power
print(math.pow(2, 3)) # 2 to the power of 3

# Maximun / Minimum infinities
float("inf")
float("-inf")
print(math.pow(2, 200) < float("inf"))

# =============================================================================
# 4. Lists, stack datastructure, slicing an unpacking
# =============================================================================
# Index: python index starts with 0, -1 is the last value
list = [1, 2, 3]
# A list in python is a dynamic array
# Use as stack data structure
# append: add value to the end of the list
list.append(4) # O(1)
print(list)
# pop: pop out the last value of the list
list.pop() # O(1)
print(list)
# Insertion O(n)
list.insert(0, 10)
print(list)
# Reasign using index
list[0] = 0
print(list)

# Initialise a list with the same value and make it of size n
n = 5
list2 = [1] * n
print(list2)

# Slicing [from, untill], the second argument is not included in the slice
# Unpacking: assign each element of a list to variables of the same number
list3 = [1, 2, 3, 4, 5]
a, b, c, d, e = list3
print(list3)

# =============================================================================
# 5. Looping through lists
# =============================================================================
# 1. using index: range(len(listname)), listname[i]
for i in range(len(list)):
    print(list[i])
# 2. without index, loop directly. syntax: for...in... 
for i in list1:
    print(i)
# 3. enumerate: loop both the index and the value
for i, n in enumerate(list):
    print(i, n)
# 4. looping through multiple arrays simultaneously
# zip function: combine two lists into pairs
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print(n1, n2)
    
# =============================================================================
# 6. Sorting
# =============================================================================
list5 = [1, 7, 3, 6, 2, 5, 4]
# reverse
list5.reverse()
print(list5)
# sort() function applies to both numbers and strings
# sort in ascending order
list5.sort()
print(list5)
# sort in descending order
list5.sort(reverse = True)
print(list5)
