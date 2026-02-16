#include<iostream>
using namespace std;

int main() {
    int e;
    cin >> e;

    int n = 9;
    int arr[n] = {1,1,1,2,2,3,3,4,4};

    int left = 0;
    int right = n - 1;
    int ans = n;

    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] >= e) {
            ans = mid;
            right = mid - 1;
        }
        else {
            left = mid + 1;
        }
    }

    if (ans == n)
        cout << "No lower bound exists\n";
    else
        cout << "Lower bound index: " << ans << endl;

    return 0;
}
