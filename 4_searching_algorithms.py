# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:22:20 2024

@author: FK
"""
# =============================================================================
# Binary search
# =============================================================================
l1 = [1, 23, 0, 18, 3, 5, 34, 8]

def binary_search(nums, target, l, r):
    m = (l + r)//2
    if l <= r:
        if nums[m] > target:
            return binary_search(nums, target, l, m-1)
        elif nums[m] < target:
            return binary_search(nums, target, m+1, r)
        elif nums[m] == target:
            return m
        else:
            return - 1
    else:
        return -1
    return binary_search(nums, target, 0, len(nums) - 1)

binary_search(l1, 5, 0, len(l1))



# In binary search, you can keep an eye of the boundry without using a real array
# Example: guess number higher or lower (Leetcode problem)
def guess_number(self, n: int) -> int:
    l, r = 1, n
    
    while True:
        m = (l + r) // 2
        result = guess(m)
        if result > 0:
            l = m + 1
        elif result < 0:
            r = m - 1
        else:
            return m


# =============================================================================
# Binary search tree
# =============================================================================
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


    def insert_into_bst(self, root, val: int):
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if val < cur.val:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    break
                cur = cur.left   
            if val > cur.val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    break
                cur = cur.right
        return root
    
