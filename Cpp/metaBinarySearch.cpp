#include <bits/stdc++.h>
#include <iostream.h>
using namespace std;


int log2(int n)
{
    int count = 0;
    while (n) {
        count++;
        n >>= 1;
    }
    return count;
}


int metaBinarySearch(vector<int> arr, int key)
{
    int n = arr.size();
    int numBits = log2(n - 1);
    int pos = 0;
    for (int shift = numBits - 1; shift >= 0; shift--) {
        int newPos = pos + 1 << shift;
        if (newPos >= n) {
            // Can't set bit to 1
        }
        else {
            if (arr[newPos] == key)
                return newPos;
            else if (arr[newPos] < key) {
                pos = newPos;
            }
        }
    }
    return -1;
}


int main()
{
    vector<int> arr{3, 4, 6, 8, 12, 14, 16};
    int key = 12;
    int index = metaBinarySearch(arr, key);
    if (index != -1)
        cout << "Key " << key << "found at: " << index << endl;
    else
        cout << "Key " << key << "not found\n!";
    return 0;
}
