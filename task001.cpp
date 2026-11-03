//
// Created by GLEB on 03.11.2026.
//
#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>

int main() {
    int n,m;
    std::cin >> n >> m;
    std::vector<std::vector<int>> matrix(n, std::vector<int>(m));
    int up,down,left,right;
    up = 0;
    down = n-1;
    left = 0;
    right = m-1;
    int sk=1;
    while (sk<=n*m) {
        for (int l = left; l<=right; l++) {
            matrix[up][l] = sk; sk++;
        }
        up++;
        for (int d = up; d<=down; d++) {
            matrix[d][right] = sk; sk++;
        }
        right--;
        if (up <=down) {
            for (int r = right; r>=left; r--) {
                matrix[down][r] = sk; sk++;
            }
            down--;
        }
        if (left <= right) {
            for (int u = down; u>=up; u--) {
                matrix[u][left] = sk; sk++;
            }
            left++;
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cout << std::setw(4)<< matrix[i][j];
        }
        std::cout << std::endl;
    }

}