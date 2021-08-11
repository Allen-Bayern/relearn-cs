#include<cstdio>
#include<vector>
#include<numeric>
#include<algorithm>
#include<cmath>
using namespace std;

int solution(vector<int> arr){
    int res = *min_element(arr.begin(), arr.end()) + accumulate(arr.begin(), arr.end(), 0);

    for(int len = 1; len < arr.size(); len++){
        if(len == 1){
            for(auto elem : arr){
                int tmp = (int)pow(elem, 2);
                if(tmp > res)
                    res = tmp;
            }
        }else{
            int start = 0;
            int terminal = len - 1;
            while(terminal < arr.size()){
                vector<int> localArea(&arr[start], &arr[terminal]);
                int tmp = *min_element(localArea.begin(), localArea.end()) + accumulate(localArea.begin(), localArea.end(), 0);
                if(tmp > res)
                    res = tmp;
                ++start;
                ++terminal;
            }
        }
    }

    return res;
}

int main(){
    int len;
    scanf("%d", &len);

    vector<int> arr;

    for(int i = 0; i < len; ++i){
        int elem;
        scanf("%d", &elem);
        arr.push_back(elem);
    }

    printf("%d", solution(arr));

    return 0;
}