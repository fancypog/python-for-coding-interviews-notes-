
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 20:32:55 2023

@author: FK
"""

# =============================================================================
# 1. Linked List
# =============================================================================
# def __init__ is the special method for constructor in python.
class Node:
    def __init__(self, data = None):
        self.data = data  # Place to store the data (None by default)
        self.next = None   # Place to store the pointer
        
class LinkedList:
    def __init__(self):
        self.head = Node() # Create a Node as the head node (empty by default)
    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != None: # Traverse through the list
            cur = cur.next
        cur.next = new_node # Append to the last one 
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)
        
# Reverse a linked list by updating the pointers
# A temporary pointer to store the poiter before you delete and update
head = LinkedList()
head.append(1)
head.append(2)
head.append(3) 
head.append(4) 
head.append(5) 

print(head)
