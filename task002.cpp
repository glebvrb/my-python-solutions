#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    int n;
    std::vector <int> A(42);
    for (int i = 1; i < 43; i++) {
        A[i - 1] = i;
    }
    int len = A.size();
    std::vector <int> B(len); B[0] = 1;
    for (int i = 2; i < 42; i++) {
        B[i - 1] = B[i - 2] + i;
    }
    int len1 = B.size();
    std::vector <int> D(len1);
    D[0] = 1;
    for (int i = 1; i < 42; i++) {
        D[i] = D[i - 1] + B[i];
    }
    D.insert(D.begin(), 0);
    std::cin >> n;
    for (int i = 1; i <= 42; i++) {
        if (n > D[i]) {
            continue;
        }
        else if (n == D[i]) {
            std::cout << i; return 0;
        }
        else {
            std::cout << i - 1; return 0;
        }
    }

}
