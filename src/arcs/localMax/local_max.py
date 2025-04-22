#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import stdin, stdout

def solution(arr):
    '''
    公式：result = min(localArea) * sum(localArea)

    局部最大值的思路：
    1. 局部至少包含1个，至多包含所有。
    也就是说，假设数组arr的长度为length。那么局部区间localArea的长度localLength必然是1<= localLength <= length。
    2. 设定两个指针start与terminal，满足start + localLength - 1 = terminal。
    然后按上一步推导，求每个满足条件的localLength下的局部区间localArea的result。
    3. 不妨先给result设定一个初值：result = min(arr) * sum(arr)，也就是全局情况下是多少。然后执行第2步。
    如果局部的result一旦大于初值，就更新。如此一来便求得。
    '''

    # initialize result
    res = min(arr) * sum(arr)

    # 用for循环执行第二步
    for length in range(1, len(arr)):
        if length == 1:
            # 如果是仅有一个变量的区间，那么公式实质上变为该数自身的平方
            for elem in arr:
                # 用临时变量捕获计算结果
                temp = elem ** 2
                if temp > res:
                    res = temp
        else:
            # 从第一个位置遍历起
            start = 0
            terminal = length - 1
            while terminal < len(arr):
                localArea = arr[start: terminal + 1 :]
                temp = min(localArea) * sum(localArea)
                if temp > res:
                    res = temp
                start += 1
                terminal += 1
    
    return res

if __name__ == '__main__':
    length = int(stdin.readline().strip())
    arr = map(int, stdin.readline().strip().split())

    stdout.write("%d"%(solution(arr)))