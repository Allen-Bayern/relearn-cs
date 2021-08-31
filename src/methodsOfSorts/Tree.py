#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sys import maxsize as MAX

# 树节点类
class TreeNode:
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None

# 树类
class Tree:
    def __init__(self):
        self.root = None 
        self.nodes = list() # 用于存放节点地址
    
    def add_single(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            self.nodes.append(self.root)
        else:
            rootNode = self.nodes[0]
            if rootNode.left is None:
                rootNode.left = TreeNode(data)
                self.nodes.append(rootNode.left)
            elif rootNode.right is None:
                rootNode.right = TreeNode(data)
                self.nodes.append(rootNode.right)
                self.nodes.pop(0) # 弹出nodes第一个元素
    
    # 有点jQuery的封装风格了
    def add_array(self, arr):
        for elem in arr:
            self.add_single(elem)