#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    int n;
    std::cin >> n;
    if (n % 2 == 0) {
        std::cout << (n * n / 2) << std::endl;
    }
    else {
        std::cout << (n / 2 + 1 + n / 2) * (n / 2) + (n / 2) + 1 << std::endl;
    }
    std::vector <std::vector<int>> matrix(n, std::vector<int>(n));
    if (1==1) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i % 2 == 0) {
                    if (j % 2 == 0) {
                        matrix[i][j] = 1;
                    }
                    else {
                        matrix[i][j] = 2;
                    }
                }
                else {
                    if (j % 2 == 0) {
                        matrix[i][j] = 2;
                    }
                    else {
                        matrix[i][j] = 1;
                    }
                }
            }
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (matrix[i][j] == 1) {
                std::cout << "C";
            }
            else {
                std::cout << '.';
            }
        }
        std::cout << std::endl;
    }

}