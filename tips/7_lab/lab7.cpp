#include <iostream>

using namespace std;

int main()
{
    const int n = 3, m = 6;
    int H[n][m] = {
        { 0, 0, 1, 1, 0, 0 },
        { 0, 1, 0, 0, 1, 0 },
        { 1, 1, 0, 0, 0, 1 }
    };
    int b[m] = { 1, 1, 0, 1, 1, 0 };

    
    cout << "------H------" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++)
            cout << H[i][j] << " ";
        cout << endl;
    }
    cout << "------B------" << endl;
    for (int j = 0; j < m; j++)
        cout << b[j] << " ";
    cout << endl;
    cout << endl;
    for (int i = 0; i < n; i++) {
        int k = 0;
        for (int j = 0; j < m; j++) {
            k += H[i][j] * b[j];
        }
        k %= 2;
        if (k != 0)
            b[i + n] = !b[i + n];
        cout << k << endl;
    }
    cout << "------B------" << endl;
    for (int j = 0; j < m; j++)
        cout << b[j] << " ";
    cout << endl;
    return 0;
}
