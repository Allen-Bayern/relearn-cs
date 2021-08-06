#include <iostream>
using namespace std;

int n, m, dp[100001], temp, a[20];

int main(){
    while(cin >> n){
        for(int i = 0; i < 100001; i++)
            dp[i] = -1;
        if(n == 0)
            break;
        
        cin >> m;

        for(int i = 0; i < m; i++){
            cin >> temp;
            a[i] = temp;
            if(temp <= n)
                dp[temp] = 1;
        }

        for(int i = 0; i <= n; i++){
            for(int j = 0; j < m; j++){
                if(a[j] < i && dp[i - a[j]] != -1){
                    if(dp[i] == -1)
                        dp[i] = dp[i - a[j]] + 1;
                    else
                        dp[i] = min(dp[i], dp[i - a[j]] + 1);
                }
            }
        }
        if(dp[n] == -1)
            cout << "Impossible" << endl;
        else
            cout << dp[n] << endl;

    }

    return 0;
}