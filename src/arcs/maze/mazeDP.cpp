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