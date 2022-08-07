#include <iostream>

using namespace std;

int main() {
    int A[5];
    for (int i=0; i<5; i++) {
        cin >> A[i];
    }

    for (int i=1; i < 1000000; i++) {
        int res = 0;
        for (int j: A) {
            if (i%j == 0) {
                res += 1;
            }
        }

        if (3 <= res) {
            cout << i;
            break;
        }
    }
}