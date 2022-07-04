# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 19:07:16 2022

@author: Kristiyan Hristov
"""
from heapq import heappush, heappop

class FindMedian:
    def __init__(self):
        """Store the smaller numbers in max heap and the bigger numbers in a min heap"""
        self.min_heap = [] 
        self.max_heap = []
        
    def insert(self, number):
        ''' Adding new element'''
        
        if not isinstance(number, int):
            if  not isinstance(number, float):
                raise ValueError("That was no valid number!  Try with either int or float!")
            else: pass
        
        # because in python the functions for heaps assume always a min heap /
        # we can moddify it to a max heap with changing the sign of the numbers
        if len(self.min_heap) == 0 or number > self.min_heap[0]:
            heappush(self.min_heap, number)
            
        else:
            heappush(self.max_heap, -number)
        
        # checks for imbalance in the lengths of the heaps
        
        #if the min heap is the bigger of the two we its smallest element (root) at put it in the max heap
        if len(self.min_heap) - len(self.max_heap) >= 2:
            heappush(self.max_heap, -heappop(self.min_heap))
            
        #if the max heap is the bigger of the two we its biggest element (root) at put it in the min heap
        if len(self.max_heap) - len(self.min_heap) >= 2:
            heappush(self.min_heap, -heappop(self.max_heap))
             
    def get_median(self):
        
        if len(self.min_heap) < len(self.max_heap):
            median = -self.max_heap[0]
            
        elif len(self.min_heap) > len(self.max_heap):
            median = self.min_heap[0]
            
        else:
            median = (self.min_heap[0] - self.max_heap[0])/2
            
        return median

#some test inputs
nums = [1, 2, 3]
nums1 = [55, 0, -88, 12]
nums2 = [15.5, 5.2, 20, 2]
strs = ['a', 'b']
lists = [[1,2], [0]]
dicts = [{'a': 0}]    
 
    
obj = FindMedian()

for num in nums2:
    obj.insert(num)
    
print(obj.get_median())

            
        