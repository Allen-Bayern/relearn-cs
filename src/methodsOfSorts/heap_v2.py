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
    
    def add_single(self, data): # 添加单个节点
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
    
    # 添加整个数组
    def add_array(self, arr):
        for elem in arr:
            self.add_single(elem)
    
    # 层序遍历，将二叉树还原为数组
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
        return res_val

# 从上面的树类派生一个堆类
class Heap(Tree):
    def __init__(self, is_max_heap = True): # 不必改变父类构造方法
        super().__init__()
        # 增加is_max_heap形参，以判定是生成最大堆还是最小堆。默认生成最大堆
        self.is_max_heap = is_max_heap
    
    # 递归重写父类的add_array方法。默认生成最大堆
    def add_array(self, arr):
        # 停止条件：如果数组为空，结束方法，并返回是否为最大堆
        if not arr:
            return self.is_max_heap
        
        # 找到数组中的最大值，并将其转化为节点（TreeNode类）
        if self.is_max_heap:
            val = max(arr)
        else:
            val = min(arr)
        node_ = TreeNode(val)

        # 调用父类的add_single()方法将其插入树中
        super().add_single(node_)
        # 删除arr中的最大值
        arr.remove(val)
        # 代入新数组，递归执行add_array方法
        self.add_array(arr)
    
    # 堆排序
    def heapsort(self):
        # 根据初始化中指定的种类是否需要反转。默认为是
        # 最终输出从小到大的数组
        if self.is_max_heap:
            return super().level_order()[::-1]
        return super().level_order()

if __name__ == '__main__':
    arr = [5, 13, 2, 25, 7, -66, 9, 12, 15]
    new_heap = Heap()
    new_heap.add_array(arr)

    # 通过层序遍历的方法将Heap类输出出来
    print(new_heap.heapsort())