#include <iostream>

using namespace std;

int main() {
    const int n = 4;
    const int m = 8;

    int G[4][8] = {
        {1, 0, 0, 0, 1, 0, 0, 0},
        {0, 1, 0, 0, 1, 0, 1, 1},
        {0, 0, 1, 0, 1, 1, 1, 0},
        {0, 0, 0, 1, 1, 1, 0, 1},

    }; 
    int H[n - 1][m];

    // for (int i = 0; i < n; i++) {
    //     for (int j = 0; j < m; j++) {
    //         if ((i == 0 && j == 0) || (i == 0 && j == 4) || (i == 0 && j == 6) || (i == 0 && j == 7) || 
    //             (i == 1 && j == 1) || (i == 1 && j == 4) || (i == 1 && j == 5) || (i == 1 && j == 6) ||
    //             (i == 2 && j == 2) || (i == 2 && j == 6) || (i == 2 && j == 7) || (i == 3 && j == 3) ||
    //             (i == 3 && j == 5) || (i == 3 && j == 6) || (i == 3 && j == 7) ) {
    //             G[i][j] = 1;
    //         }
    //         else {
    //             G[i][j] = 0;
    //         }
    //     }
    // }
    cout << "------G------" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << G[i][j] << " ";
        }
        cout << endl;
    }
    cout << "------H------" << endl;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            if (j < n) {
                H[i][j] = G[j][i + n];
            } else {
                if (i + 4 == j) {
                    H[i][j] = 1;
                }
                else {
                    H[i][j] = 0;
                }
            }
        }
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            cout << H[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}