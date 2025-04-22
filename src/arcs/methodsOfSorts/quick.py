#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def quick_sort(arr):
    if (not arr) or len(arr) == 1:
        # 如果arr是空数组或单元素数组，那么直接return它自身即可
        return arr

    # 选中基准点为最右一位
    pivot = arr[-1]
    # 建立空数组left和right
    left, right = list(), list()

    for elem in arr[:len(arr) - 1:]:
        # 像上面这样写可以保证不遍历到最后一位
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == '__main__':
	print(quick_sort([2,1,5,3,8,4,9,5]))