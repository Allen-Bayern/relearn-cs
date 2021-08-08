#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def partition(ar, l, h):
    if h < l: # 以防输错。输错就交换一下
        h, l = l, h
    
    pivot = ar[h]
    i = l - 1
    
    for j in range(l, h):
        if ar[j] <= pivot:
            i += 1
            ar[i], ar[j] = ar[j], ar[i]
    
    ar[h], ar[i + 1] = ar[i + 1], ar[h]
    
    return i + 1

def quicksort(ar, l, h): # 执行快速排序的过程
    if l < h:
        pi = partition(ar, l, h)
        quicksort(ar, l, (pi - 1))
        quicksort(ar, (pi + 1), h)

if __name__ == "__main__":
    a = [1, 7, 2, 88, 3, 6, 12]
    len_ = len(a)
    quicksort(a, 0, (len(a) - 1))
    for i in range(len_):
        print("%d"%a[i])