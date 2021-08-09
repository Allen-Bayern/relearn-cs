#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 代码有问题，不能运行

def quick_sort(arr):
    if (not arr) or (len(arr) == 1):
        return arr 
    
    arr_aux = [0 for _ in range(len(arr))]

    while True:
        pivot_index = len(arr) - 1
        for i in range(len(arr) - 1):
            if arr_aux[i] == 1:
                continue
            if arr[i] > arr[pivot_index]:
                arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
                pivot_index = i
        
        arr_aux[pivot_index] = 1

        if sum(arr_aux) == len(arr):
            break
    
    return arr 

if __name__ == '__main__':
	print(quick_sort([2,1,5,3,8,4,9,5]))