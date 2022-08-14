#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(){
    string a,b;

    cin >> a >> b;

    int n = b.length()-a.length();
    int res = 987654321;

    for (int i=0; i<=n; i++) {
        int r = 0;
        for (int j=i; j<a.length()+i; j++) {
            if (a[j-i] != b[j]) {
                r ++;
            }
        }

        res = min(res, r);
    }

    cout << res;

    return 0;
}