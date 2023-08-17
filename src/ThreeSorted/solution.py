#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution_func(arr1: list[int], arr2: list[int], arr3: list[int]):
    # 边界条件，只要有一个是空的就返回空的
    if 0 in list(map(len, [arr1, arr2, arr3])):
        return list()
    
    hash_map: dict[int, int] = dict()
    
    for i in range(len(arr1)):
        num = arr1[i]
        if not (num in hash_map):
            hash_map[num] = 1
    
    for i in range(len(arr2)):
        num = arr1[i]
        if not (num in hash_map):
            hash_map[num] = 1
        elif hash_map[num] == 2:
            continue
        else:
            hash_map[num] = +1
    
    for i in range(len(arr3)):
        num = arr1[i]
        if not (num in hash_map):
            hash_map[num] = 1
        elif hash_map[num] == 3:
            continue
        else:
            hash_map[num] = +1
    
    res: list[int] = list()
    
    for key in hash_map.keys():
        if hash_map[key] == 3:
            res.append(key)
    
    return res