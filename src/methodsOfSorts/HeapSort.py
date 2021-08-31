#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize as MAX

class Heap:
    def __init__(self, heap = list()):
        '''
        :param heap: an Array
        '''
        self.heap = heap
    
    def parent_index(self, i):
        if (i // 2 - 1) >= 0:
            return (i // 2 - 1)
        return -MAX
    
    def left_index(self, i):
        if (2 * i + 1) < len(self.heap):
            return (2 * i + 1)
        return -MAX
    
    def right_index(self, i):
        if (2 * (i + 1)) < len(self.heap):
            return (2 * (i + 1)) 
        return -MAX
    
    def has_property(self, prop, i):
        '''
        :param prop: parent_index、left_index、right_index中的任意一种
        :param i: 第i个节点的下标
        返回值为True或False
        '''
        if prop(i) == -MAX:
            return False 
        return True
    
    def max_heapify(self, n, i):
        largest = i # 默认第i个为最大

        # 如果有左节点
        if self.has_property(self.left_index, i):
            l = self.left_index(i)
            if l <= n and self.heap[l] > self.heap[i]:
                largest = l
        
        # 如果有右节点
        if self.has_property(self.left_index, i): 
            r = self.right_index(i)
            if r <= n and self.heap[r] > self.heap[i]:
                largest = r 
        
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(n, largest)
    
    def heapsort(self):
        n = len(self.heap)
        for i in range(n, -1, -1):
            self.max_heapify(n, i)
    
        for i in range(len(self.heap) - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            n -= 1
            self.max_heapify(n, 0)

if __name__ == '__main__':
    arr = [5, 13, 2, 25, 7, -66, 9, 12, 15]
    new_heap = Heap(arr)
    new_heap.heapsort()
    print(new_heap.heap)