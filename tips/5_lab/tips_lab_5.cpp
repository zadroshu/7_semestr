

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int length = 10;
    double arr[length][length];
    double H[length];
    for (int i = 0; i < length; i++){
        H[i] = 0;
        for (int j = 0; j < length; j++){
            arr[i][j] = 0;
        }
    }
    arr[0][1] = 1.0/3;
    arr[0][2] = 1.0/3;
    arr[0][3] = 1.0/3;
    arr[1][4] = 1.0/3;
    arr[1][5] = 1.0/3;
    arr[1][6] = 1.0/3;
    arr[2][7] = 1.0/3;
    arr[2][8] = 1.0/3;
    arr[3][9] = 1.0/3;
    
    H[1] = -(arr[0][1] * std::log2(arr[0][1]));
    H[2] = -(arr[0][2] * std::log2(arr[0][2]));
    H[3] = -(arr[0][3] * std::log2(arr[0][3]));
    
    H[4] = H[1] -(arr[1][4] * std::log2(arr[1][4]));
    H[5] = H[1] -(arr[1][5] * std::log2(arr[1][5]));
    H[6] = H[1] -(arr[1][6] * std::log2(arr[1][6]));
    
    H[7] = H[2] -(arr[2][7] * std::log2(arr[2][7]));
    H[8] = H[2] -(arr[2][8] * std::log2(arr[2][8]));
    
    H[9]  = H[3] -(arr[3][9] * std::log2(arr[3][9]));
    
    cout<< "Энтропия событий равна:" << endl;
    for (int i = 0; i < length; i++){
        
        cout << "H(" << i << ") = " << H[i] << endl;
    }
    
    return 0;
}
