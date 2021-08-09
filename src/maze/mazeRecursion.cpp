#include <vector>
#include <cstdio>
#include <numeric>
#include <algorithm>
using namespace std;

int solution(vector<vector<int>> maze){
    if(maze.empty())
        return 0;

    if(maze.size() == 1)
        return accumulate(maze[0].begin(), maze[0].end(), 0);
    
    if(maze[0].size() == 1){
        auto res = 0;
        for(vector<int> pane : maze)
            res += pane[0];
        
        return res;
    }

    // 向右访问之后的子向量
    vector<vector<int>> rightSub;
    for(vector<int> row : maze){
        vector<int> everyRow {row.begin() + 1, row.end()};
        rightSub.push_back(everyRow);
    }

    // 向下访问之后的子向量
    vector<vector<int>> downSub {maze.begin() + 1, maze.end()};

    return maze[0][0] + min(solution(downSub), solution(rightSub));
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