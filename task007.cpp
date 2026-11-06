#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    std::cin.ignore();
    std::string s;
    std::vector<std::vector<int>> A(n, std::vector<int>(n));
    for (int i = 0; i < n; i++) {
        std::getline(std::cin, s);
        for (int y = 0; y < s.size(); y++) {
            if (s[y] == 'X') {
                A[i][y] = 1;
            }
        }
    }
    int mi = 0; int mj = 0; int d0 = 0; int d1 = 0;
    int ts = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (A[i][j] == 1) {
                ts++; mi = std::max(mi, ts);
            }
            else {
                ts = 0;
            }
        }
        ts = 0;
    }
    ts = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (A[j][i] == 1) {
                ts++; mj = std::max(mj, ts);
            }
            else {
                ts = 0;
            }
        }
        ts = 0;
    }
    ts = 0;
    for (int su = 0; su <= 2 * n - 2; su++) {
        for (int str = 0; str <= n-1; str++) {
            int st = su - str;
            if (st >= 0 and st <= n - 1) {
                if (A[str][st] == 1) {
                    ts++; d0 = std::max(d0, ts);
                }
                else {
                    ts = 0;
                }
            }

        }
        ts = 0;
    }
    ts = 0;
    for (int r = -(n - 1); r <= n - 1; r++) {
        for (int str = 0; str <= n-1;str++) {
            int st = str - r;
            if (st >= 0 && st <= n - 1) {
                if (A[str][st] == 1) {
                    ts++; d1 = std::max(d1, ts);
                }
                else {
                    ts = 0;
                }
            }
            else {
                continue;
            }
        }
        ts = 0;
    }
    int u = std::max(mi, mj);
    int u1 = std::max(d0, d1);
    std::cout << std::max(u, u1); return 0;
}