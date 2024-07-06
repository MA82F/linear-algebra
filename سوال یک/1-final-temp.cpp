#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

vector<vector<float>> matrix;

void get_matrix_input() {
    int n;
    cin >> n;
    matrix.resize(n, vector<float>(n));

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }
}

int calculate_determinant(vector<vector<float>> mat) {
    int n = mat.size();
    if (n == 1) {
        return mat[0][0];
    } else if (n == 2) {
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0];
    } else {
        float determinant = 0;
        for (int c = 0; c < n; ++c) {
            if (mat[0][c] == 0) {
                return 0;
            }
            vector<vector<float>> submat(n - 1, vector<float>(n - 1));
            for (int i = 1; i < n; ++i) {
                int subcol = 0;
                for (int j = 0; j < n; ++j) {
                    if (j == c) continue;
                    submat[i - 1][subcol] = mat[i][j];
                    subcol++;
                }
            }
            determinant += pow(-1, c) * mat[0][c] * calculate_determinant(submat);
        }
        return determinant;
    }
}

int main() {
    get_matrix_input();
    if (!matrix.empty()) {
        float determinant = calculate_determinant(matrix);
        cout << static_cast<int>(determinant) << endl;
    }
    return 0;
}
