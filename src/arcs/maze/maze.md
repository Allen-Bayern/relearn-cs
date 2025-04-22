# 美团走迷宫题 

> 链接：https://www.nowcoder.com/questionTerminal/2a38bd658ba04a1dbd006107c51ff14e
> 来源：牛客网

给定一个包含非负整数的 M x N 迷宫，请找出一条从左上角到右下角的路径，使得路径上的数字总和最小。每次只能向下或者向右移动一步。


输入描述:
第一行包含两个整数M和N，以空格隔开，1≤N≤10，1≤N≤10。接下来的M行中，每行包含N个数字 。

输出描述:
找出总和最小的路径，输出路径上的数字总和。

示例1

输入
```Python
3 3
1 3 1
1 5 1
4 2 1
```

输出
```Python
7
```

## 思路解析

仔细分析一番便可看出，此题可以**递归**求解。思路如下：

* 只要能拆成子问题的题目就可以用递归。在本题中，子问题是如果迷宫只有一行或者只有一列，该怎么走？
* 只有一列的情况：有n行，即数组长度为n。但这n行的子数组每个只有一个元素。只需要将每一行的元素相加即可；
* 只有一行的情况：将数组内唯一一个子数组中所有元素相加即可。
* 递归写法：只需要从`maze[0][0]`出发，看是走向右一步的子数组值更小，还是向下一步的值更小。

代码如下：

```Python
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

    # expected output: 7
    print(solution(maze))
```

只不过递归**一定会超时**。

## 上述代码优化

用一个额外空间，存储从`maze[0][0]`出发到每个格子的最小数值：
* 设`maze`本身是一个M * N的数组。那么申请一个同样大小的`aux`数组。
* `aux`第一行的第一列值的求法和上面递归法是一样的。
* 将上面的递归式改为状态转移方程：即，从上面过来最小还是从左边过来最小。这样一来便保证每一格存的都是最优解。
* 将`aux[m-1][n-1]`作为返回值。

代码如下：

```C++
#include<vector>
#include<algorithm>
#include<cstdio>
using namespace std;

int solution(vector<vector<int>> &maze){
    const int m = maze.size();
    const int n = maze[0].size();

    vector<vector<int>> aux(m, vector<int>(n, 0));

    aux[0][0] = maze[0][0];

    for(int i = 1; i < m; i++)
        aux[i][0] = aux[i - 1][0] + maze[i][0];
    
    for(int j = 1; j < n; j++)
        aux[0][j] = aux[0][j - 1] + maze[0][j];
    
    for(int i = 1; i < m; i++){
        for(int j = 1; j < n; j++)
            aux[i][j] = maze[i][j] + min(aux[i - 1][j], aux[i][j - 1]);
    }

    return aux[m - 1][n - 1];
}

int main(){

    vector<vector<int>> maze = {
        {1, 3, 1},
        {1, 5, 1},
        {4, 2, 1}
    };

    printf("%d\n", solution(maze));
    return 0;
}
```