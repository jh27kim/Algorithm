#include <iostream>

using namespace std;
int tree[10001];

void dfs(int start, int end) {
	if (start >= end) {
		return;
	}

	if (start == end - 1) {
		cout << tree[start] << endl;
		return;
	}

	int idx = start;
	while (idx < end) {
		if (tree[idx] > tree[start]) {
			break;
		}
		idx++;
	}

	dfs(start + 1, idx);
	dfs(idx, end);
	cout << tree[start] << endl;

	return;
}

int BinarySearchTree() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	int num;
	int idx = 0;

	while (cin >> num) {
		tree[idx++] = num;
	}
	dfs(0, idx);

	
	return 0;
}