#include <iostream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

vector<vector<double>> matrix;

void get_matrix_input() {
    int n;
    cin >> n;
    cin.ignore();
    for (int i = 0; i < n; i++) {
        string line;
        getline(cin, line);
        istringstream iss(line);
        vector<double> row;
        double number;
        while (iss >> number) {
            row.push_back(number);
        }
        matrix.push_back(row);
    }
}

double calculate_determinant(vector<vector<double>> mat) {
    int n = mat.size();
    if (n == 1) {
        return mat[0][0];
    } else if (n == 2) {
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
    } else {
        double determinant = 0;
        for (int c = 0; c < n; c++) {
            if (mat[0][c] == 0) {
                return 0;
            }
            vector<vector<double>> submatrix;
            for (int i = 1; i < n; i++) {
                vector<double> row;
                for (int j = 0; j < n; j++) {
                    if (j != c) {
                        row.push_back(mat[i][j]);
                    }
                }
                submatrix.push_back(row);
            }
            determinant += pow(-1, c) * mat[0][c] * calculate_determinant(submatrix);
        }
        return determinant;
    }
}

int main() {
    get_matrix_input();
    if (!matrix.empty()) {
        double determinant = calculate_determinant(matrix);
        printf("%.2f\n", determinant);
    }
    return 0;
}
