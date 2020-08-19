"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# import sys
# sys.path.enqueue('/Users/thiernodiallo/Documents/Code/CS/part1/Data-Structures/queue/queue.py')
# sys.path.enqueue('/Users/thiernodiallo/Documents/Code/CS/part1/Data-Structures/stack/stack.py')
# from stack import *
from queue import MyQueue
from stack import MyStack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self is None:
            self = BSTNode(value)
        else:
            if value >= self.value:
                if self.right is None:
                    self.right = BSTNode(value)
                else:
                    self.right.insert(value) 
            elif value < self.value:
                if self.left is None:
                    self.left = BSTNode(value)
                else:
                    self.left.insert(value) 


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        found = False
        if self:
            if target == self.value:
                return True 
            if target < self.value:
                if self.left is None:
                    return False
                found = self.left.contains(target)
            else:
                if self.right is None:
                    return False
                found = self.right.contains(target)
        else:
             found = False
        return found
        
        

    # Return the maximum value found in the tree
    def get_max(self):
        if self:
            if self.right:
                return self.right.get_max()
            return self.value
            
        else:
            return None


    # Call the function `fn` on the value of each node
    # call function on the current value fn(self.value)
    # if you can go left, call for_each on the left tree
    # if you can go right, call for_each on the right tree
    def for_each(self, fn):
        if self:
            fn(self.value)
            if self.left:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)  
        else:
            return None 
        
    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self,node):
            if node.left:
                node.left.in_order_print(node.left)
            print(node.value)
            if node.right:
                node.right.in_order_print(node.right)
       

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    def bft_print(self,node):
        if node:
            queue = MyQueue()
            queue.enqueue(node) 
            while len(queue) > 0:
                current = queue.dequeue()
                print(current.value)
                if current.left:
                    queue.enqueue(current.left)
                if current.right:
                    queue.enqueue(current.right)
        else:
            return None 

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    def dft_print(self, node):
        if node:
            stack = MyStack()
            stack.push(node) 
            while len(stack) > 0:
                current = stack.pop()
                print(current.value)
                if current.left:
                    stack.push(current.left)
                if current.right:
                    stack.push(current.right)
        else:
            return None 

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            node.left.pre_order_dft(node.left)
        if node.right:
            node.right.pre_order_dft(node.right)
      

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            node.left.post_order_dft(node.left)
        if node.right:
            node.right.post_order_dft(node.right)
        print(node.value)
        
        
