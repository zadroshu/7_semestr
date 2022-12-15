/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <cmath>
using namespace std;

int
main (){
  double a[] = { 1, 1.8, 2, 3.6, 3.9, 4.1, 5 };
  double sum = 0, mean = 0, kv_mean = 0;
  for (int i = 0; i < 7; i++)
    {
      sum += a[i];
    }
  mean = sum / 7;

  for (int i = 0; i < 7; i++)
    {
      kv_mean += (a[i] - mean) * (a[i] - mean);
    }
  kv_mean = sqrt (kv_mean / 7);

  double quan[7];
  double persent = (1.0 / 7);
  for (int i = 0; i < 7; i++){
      quan[i] = (i + 1) * persent * (a[6]);
    }
  cout << "Sum = " << sum << endl;
  cout << "Mean = " << mean << endl;
  cout << "KV_mean = " << kv_mean << endl;
  cout << "Median = " << a[7 / 2] << endl;
  cout << "Quant = ";
  for (int i = 0; i < 7; i++){
      cout <<  quan[i] << +" ";
    }

  return 0;
}
