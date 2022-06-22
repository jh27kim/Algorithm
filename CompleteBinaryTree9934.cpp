#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

int n;
int arr[1025];
vector<int> v[10];

void dfs(int depth, int start, int end) {
	if (start >= end) {
		return;
	}

	int mid = (start + end) / 2;
	v[depth].push_back(arr[mid]);
	dfs(depth + 1, start, mid);
	dfs(depth + 1, mid + 1, end);
}

int CompleteBinaryTree9934() {
	cin >> n;
	
	for (int i = 0; i < pow(2, n)-1;i++) {
		cin >> arr[i];
	}

	dfs(0, 0, pow(2, n)-1);

	for (int i = 0; i < n; i++) {
		for (auto elem : v[i]) {
			cout << elem << " ";
		}
		cout << "\n";
	}

	return 0;
}