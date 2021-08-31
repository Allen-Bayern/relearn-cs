#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize as MAX

# 定义空值异常
class EmptyValueError(Exception):
    def __init__(self, obj):
        self.object = obj
    
    def __str__(self):
        if self.object is None:
            return 'The value of the object is empty!!!'

# 树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

# 树类
class Tree:
    def __init__(self, arr = list()):
        try:
            if not arr: # 抛出错误
                raise EmptyValueError
            self.root = TreeNode(arr[0])
            for 
        except EmptyValueError:
            print('Please re-transform a non-empty array.')