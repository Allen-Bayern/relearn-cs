#!/usr/bin/python
# coding: utf-8

'''
:description: 二叉树层序遍历
'''

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def order_traversal(root):
    if not root:
        return []
    
    queue = deque()
    queue.append(root)
    
    res = list()
    while len(queue):
        size = len(queue)
        tmp = list()
        
        for _ in range(size):
            current_node = queue.popleft();
            tmp.append(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        res.append(tmp)
    
    return res