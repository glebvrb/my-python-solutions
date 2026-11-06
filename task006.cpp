#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>



int main() {
    int n, m, k;
    std::vector<std::pair<int, int>> P{ { -1,1 },{ -1,0 },{ -1,-1 },{ 1,1 },{ 1,-1 },{ 1,0 },{ 0,1 },{ 0,-1 } };
    std::cin >> n >> m >> k;
    std::vector <std::vector<int>> M(n, std::vector<int>(m));
    int q, w;
    for (int i = 0; i < k; i++) {
        std::cin >> q >> w;
        M[q - 1][w - 1] = 10;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            int ms = 0;
            for (int e = 0; e <= 7; e++) {
                int k1 = P[e].first; int k2 = P[e].second;
                if (i + k1 >= 0 && i + k1 <= n - 1 && j + k2 >= 0 && j + k2 <= m - 1) {
                    if (M[i + k1][j + k2] == 10) {
                        ms++;
                    }
                }
            }
            if (M[i][j] != 10) {
                M[i][j] = ms;
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (M[i][j] == 10) {
                std::cout << '*';
            }
            else if (M[i][j] == 0) {
                std::cout << '.' ;
            }
            else {
                std::cout << M[i][j];
            }
        }
        std::cout << std::endl;
    }
}