#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>


bool check(std::vector<int> A) {
    bool fl = true;
    for (int i = 0; i < A.size() / 2; i++) {
        if (A[i] != A[A.size() - 1 - i]) {
            fl = false;
        }
    }
    if (fl) {
        return true;
    }
    return false;
}



int main() {
    int n;
    std::cin >> n;
    std::vector <int> A(n);
    for (int i = 0; i < n; i++) {
        std::cin >> A[i];
    }

    if (check(A)) {
        std::cout << 0; return 0;
    }
    std::vector <int> OT;
    int ku = 1;
    for (int i = ku; i <= n - 1; i++) {
        int e = A[0];
        A.erase(A.begin());
        if (check(A)) {
            OT.push_back(e); break;
        }
        ku++; OT.push_back(e);
    }
    std::cout << ku << std::endl;
    std::reverse(OT.begin(), OT.end());
    for (auto w : OT) {
        std::cout << w << ' ';
    }
    return 0;
}