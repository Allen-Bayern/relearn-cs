#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solution(maze):
    # 如果是空迷宫，直接返回0
    if not maze:
        return 0
    
    # 递归停止条件1：只有1行的迷宫
    if len(maze) == 1:
        return sum(maze[0])
    
    # 递归停止条件2：只有1列的迷宫
    if len(maze[0]) == 1:
        res = 0
        for pane in maze:
            res += pane[0]
        
        return res
    
    return maze[0][0] + min(solution(maze[1::]), solution([row[1::] for row in maze]))

if __name__ == '__main__':
    maze = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]

    print(solution(maze))