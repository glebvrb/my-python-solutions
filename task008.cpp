#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>


void solve() {
    int n;
    std::cin >> n; int e;
    std::vector <std::vector <int>> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> e; A[i] = { e,i,0 };
    }
    std::stable_sort(A.begin(), A.end());
    if (n == 1) {
        std::cout << -1 << "\n"; return;
    }
    for (int i = 0; i < n - 2; i++) {
        for (int t = 0; t < n; t++) {
            if (A[t][2] == 0 && A[t][1] != i) {
                std::cout << A[t][0] << " "; A[t][2] = 1; break;
            }
        }
    }
    int u1, u2; int n1, n2;
    for (int i = 0; i < n; i++) {
        if (A[i][2] == 0) {
            u1 = A[i][0]; n1 = A[i][1]; A[i][2] = 1;break;
        }
    }
    for (int i = 0; i < n; i++) {
        if (A[i][2] == 0) {
            u2 = A[i][0]; n2 = A[i][1];  break;
        }
    }
    if (u1 < u2 && n1 != n - 2 && n2!=n-1) {
        std::cout << u1 << ' ' << u2 << "\n"; return;
    }
    else {
        std::cout << u2 << ' ' << u1 << "\n"; return;
    }
}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int t;
    std::cin >> t;
    for (int j = 0; j < t; j++) {
        solve();
    }
}