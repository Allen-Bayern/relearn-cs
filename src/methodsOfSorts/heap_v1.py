#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def heapify(arr, i):
    largest = i

    left = 2 * i + 1
    right = 2 * (i + 1)

    if left < arrL and arr[left] > arr[largest]:
        largest = left 
    
    if right < arrL and arr[right] > arr[largest]:
        largest = right 
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest)

def build(arr):
    for i in range(len(arr) // 2, -1, -1):
        heapify(arr, i)

def heapsort(arr):
    global arrL 
    arrL = len(arr)
    build(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        arrL -= 1
        heapify(arr, 0)
    
    return arr 

if __name__ == '__main__':
    arr = [5, 13, 2, 25, 7, -66, 9, 12, 15]
    print(heapsort(arr))