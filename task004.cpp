#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    int n, x;
    std::cin >> n >> x;
    int x1, x2;
    std::vector <std::pair<int, int>> W(n);
    for (int i = 0; i < n; i++) {
        std::cin >> x1 >> x2;
        if (x1 > x2) {
            int y1 = x1; int y2 = x2;
            x1 = y2; x2 = y1;
            W[i] = { x1,x2 };
        }
        else {
            W[i] = { x1,x2 };
        }
    }
    std::vector <int> P;
    for (int i = 0; i <= 1000; i++) {
        bool f = true;
        for (int e = 0; e < W.size(); e++) {
            if (!f) {
                break;
            }
            else if (i >= W[e].first && i <= W[e].second) {
                continue;
            }
            else {
                f = false;
            }

        }
        if (f) {
            P.push_back(i);
        }
        else {
            continue;
        }
    }
    int mr = 999999;
    if (P.empty()) {
        std::cout << -1; return 0;
    }
    for (auto y : P) {
        if (abs(x - y) < mr) {
            mr = abs(x - y);
        }
    }
    std::cout << mr; return 0;
}