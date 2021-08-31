#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
    
    # 层序遍历
    def level_order(self):
        if not self.root:
            return list()
        
        res = list()

        def DFS(node, dph = 0):
            if node:
                while len(res) <= dph:
                    res.append(list())
                res[dph].append(node.value)
                DFS(node.left, dph + 1)
                DFS(node.right, dph + 1)
        
        DFS(self.root)
        res_val = list()
        for elem in res:
            res_val.append(elem[0].value)
        return res_val.reverse()

class Heap(Tree):
    def __init__(self):
        super().__init__()
    
    def add_array(self, arr):
        if not arr:
            return 
        
        max_val = max(arr)
        max_node = TreeNode(max_val)
        super().add_single(max_node)
        arr.remove(max_val)
        self.add_array(arr)

if __name__ == '__main__':
    arr = [5, 13, 2, 25, 7, -66, 9, 12, 15]
    new_heap = Heap()
    new_heap.add_array(arr)
    print(new_heap.level_order())