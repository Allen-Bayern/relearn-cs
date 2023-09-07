#!/usr/bin/python
# -*- coding: utf-8 -*-

from copy import deepcopy

# 计数排序
def count_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return deepcopy(arr)
    
    min_value = min(arr)
    max_value = max(arr)
    
    count_list = [0 for i in range(max_value - min_value + 1)]
    
    for num in arr:
        count_list[num - min_value] += 1
    
    result: list[int] = list()
    
    for i in range(len(count_list)):
        current_time = count_list[i]
        current_value = min_value + i
        
        if not current_time:
            continue
        else:
            for j in range(current_time):
                result.append(current_value)
    
    return result

if __name__ == '__main__':
    print(count_sort([-19, 22, 3, 765, -421, 1, 2 + 8]))