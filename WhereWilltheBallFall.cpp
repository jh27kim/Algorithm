#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector <int> ans;
    void find(vector<vector<int>>& grid, int i, int j, int r, int c) {
        if (i == r) {
            ans.push_back(j);
            return;
        }

        if (grid[i][j] == -1) {
            if (j == 0 || grid[i][j - 1] != -1) {
                ans.push_back(-1);
                return;
            }
            else {
                find(grid, i + 1, j - 1, r, c);
            }
        }
        else {
            if (j == c - 1 || grid[i][j + 1] != 1) {
                ans.push_back(-1);
                return;
            }
            else {
                find(grid, i + 1, j + 1, r, c);
            }
        }
    }


    vector<int> findBall(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();

        for (int i = 0; i < c; i++) {
            find(grid, 0, i, r, c);
        }
        return ans;
    }
};