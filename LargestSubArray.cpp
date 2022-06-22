#include <iostream>
#include <vector>

using namespace std;

int arr[10000];
int N;

int findmax(int start, int end) {
	if (start >= end) {
		return arr[start];
	}

	int mid = (start + end) / 2;
	int a = findmax(start, mid);
	int b = findmax(mid + 1, end);

	int maxLeft = 0;
	int sum = 0;
	for (int i = mid; i >= start; i--) {
		sum = sum + arr[i];
		maxLeft = max(sum, maxLeft);
	}

	int maxRight = 0;
	int sum = 0;
	for (int i = mid + 1;i <= end;i++) {
		sum = sum + arr[i];
		maxRight = max(maxRight, sum);
	}

	return max(max(maxRight, maxLeft), maxRight + maxLeft);
}


int main() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	cout << findmax(0, N - 1);


	return 0;
}