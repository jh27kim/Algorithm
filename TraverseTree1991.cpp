#include <iostream>

using namespace std;

int lst[50][2];

void preorder(int N) {
	if (N == -1) return;
	cout << (char)(N+'A');
	preorder(lst[N][0]);
	preorder(lst[N][1]);
}

void inorder(int N) {
	if (N == -1) return;
	inorder(lst[N][0]);
	cout << (char)(N + 'A');
	inorder(lst[N][1]);
}

void postorder(int N) {
	if (N == -1) return;
	postorder(lst[N][0]);
	postorder(lst[N][1]);
	cout << (char)(N + 'A');
}


int TraverseTree1991() {
	int n;
	cin >> n;

	for (int i = 0; i < n; i++) {
		char x, y, z;
		cin >> x >> y >> z;
		x = x - 'A';
		if (y == '.') {
			lst[x][0] = -1;
		}
		else {
			lst[x][0] = y - 'A';
		}

		if (z == '.') {
			lst[x][1] = -1;
		}
		else {
			lst[x][1] = z - 'A';
		}
	}

	preorder(0);
	cout << endl;
	inorder(0);
	cout << endl;
	postorder(0);

	return 1;
}
