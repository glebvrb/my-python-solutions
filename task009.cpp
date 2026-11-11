#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <set>
#include <string>
#include <map>

/*
void solve() {
    here will be the solution
}
*/


bool compare( const std::vector<int>& a, const std::vector<int>& b) {
    return a[1] < b[1];

}


int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    int n;
    std::cin >> n; int e, w;
    std::vector <std::vector <int>> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> e >> w;
        if (e > w) {
            A[i] = { w,e };
        }
        else {
            A[i] = { e,w };
        }
    }
    std::sort(A.begin(), A.end(), compare);
    std::vector <int> T;
    int ln = A[0][1]; T.push_back(A[0][1]);
    for (int i = 1; i < n; i++) {
        if (A[i][0] > ln) {
            ln = A[i][1]; T.push_back(ln);
        }
    }
    std::cout << T.size() << "\n";
    for (auto y : T) {
        std::cout << y << ' ';
    }
    return 0;

}