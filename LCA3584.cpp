#include <iostream>
#include <vector>

using namespace std;

int T;
int N;
vector<int> child[10002];
int parent[10002];
vector<int> depth;

void find_depth(int cur, int x, int d) {
	for (int i = 0; i < child[cur].size(); i++) {
		//cout << "searching" << child[cur].at(i) <<endl;
		if (child[cur].at(i) == x) {
			depth.push_back(d);
			return;
		}
		find_depth(child[cur].at(i), x, d+1);
	}
}

void init() {
	for (int i = 0; i < 10002; i++) {
		parent[i] = 0;
		child[i].clear();
	}
	depth.clear();
}

int LCA() {
	cin >> T;
	for (int i = 0; i < T; i++) {
		cin >> N;
		init();
		for (int j = 0; j < N-1; j++) {
			int a, b;
			cin >> a >> b;
			child[a].push_back(b);
			parent[b] = a;
		}

		int x, y;
		cin >> x >> y;

		int root = 0;
		for (int i = 1;i < N + 1; i++) {
			if (!parent[i]) {
				root = i;
				break;
			}
		}

		//cout << "Root: " << root << endl;
		find_depth(root, x, 1);
		find_depth(root, y, 1);

		//cout << "Query" << x << y << endl;

		//cout << "----------------" << endl;
		//cout << depth[0] << endl;
		//cout << depth[1] << endl;
		//cout << "----------------" << endl;

		//cout << "Diff depth " <<  abs(depth[0] - depth[1]) << endl;
		for (int i = 0; i < abs(depth[0] - depth[1]); i++) {
			if (depth[0] > depth[1]) {
				x = parent[x];
			}
			else {
				y = parent[y];
			}
		}

		//cout << "Escalated X, Y" << x << y << endl;

		if (x == y) {
			cout << x << endl;
		}
		else {
			while (min(depth[0], depth[1])) {
				x = parent[x];
				y = parent[y];
				if (x == y) {
					cout << x << endl;
					break;
				}
			}
		}


	}
	return 0;
	
}