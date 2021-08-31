#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize as MAX

class Heap:
    def __init__(self, heap = list()):
        '''
        :param heap: an Array
        '''
        self.heap = heap
        self.size = len(self.heap)
    
    def parent_index(self, i):
        if (i // 2 - 1) < 0:
            return -MAX
        return (i // 2 - 1)
    
    def left_index(self, i):
        if (2 * i + 1) >= self.size:
            return -MAX
        return (2 * i + 1)
    
    def right_index(self, i):
        if (2 * (i + 1)) >= self.size:
            return -MAX
        return (2 * (i + 1))
    
    # 适配层
    def has_property(self, method, i):
        if method(i) == -MAX:
            return False 
        return True    
    
    def max_heapify(self, i):
        # 递归停止条件
        if self.size == 1:
            return 

        largest = i # 默认第i个为最大

        if self.has_property(self.left_index, i):
            l = self.left_index(i)
            if l <= self.size and self.heap[l] > self.heap[i]:
                largest = l
        
        if self.has_property(self.left_index, i):
            r = self.right_index(i)
            if r <= self.size and self.heap[r] > self.heap[i]:
                largest = r 
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i] 
        
        # 上溯
        if self.has_property(self.parent_index, i):
            dad = self.parent_index(i)
            self.max_heapify(dad)
    
    def build(self):
        for i in range(self.size // 2, -1, -1):
            self.max_heapify(i)
    
    def heapsort(self):
        self.build()
        for i in range(self.size - 1, 1, -1):
            self.heap[1], self.heap[i] = self.heap[i], self.heap[1]
            new_heap = Heap(self.heap[2::])
            new_heap.max_heapify(1)
    
if __name__ == '__main__':
    arr = [5, 13, 2, 25, 7, 17, 20, 8, 4]
    new_heap = Heap(arr)
    new_heap.heapsort()
    print(new_heap.heap)