#include <bits/stdc++.h>
using namespace std::chrono;
using namespace std;



//Recurrance Relation = 3T(n/2)+nlogn

//Using Master Theorem Case 1 : a > b^k = O(n^(log(base2)a))

//Time Complexity = O(n^(log(base2)3))


void complexRec(int n) {

   if (n <= 2) {
       return;
   }

   int p = n;
   while (p > 0) {
       vector<int> temp(n);
       for (int i = 0; i < n; i++) {
           temp[i] = i ^ p;
       }
       p >>= 1;
   }

   vector<int> small(n);
   for (int i = 0; i < n; i++) {
       small[i] = i * i;
   }

   if (n % 3 == 0) {
       reverse(small.begin(), small.end());
   } else {
       reverse(small.begin(), small.end());
   }

   complexRec(n / 2);
   complexRec(n / 2);
   complexRec(n / 2);
}

int main() {
    
    int n = 1024;

    auto start = high_resolution_clock::now();

    complexRec(n);

    auto end = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(end - start);
    cout << "Time for n = " << n << " : "
         << duration.count() << " ms\n";

    return 0;
}