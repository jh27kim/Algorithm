package AdHocAlgorithms;

public class KthElementinSortedArrays {
    public static int solution(int [] arr1, int [] arr2, int k) {
        int l = Math.max(arr2.length-k, 0);
        int r = arr1.length;
        int mid; int p=0;
        int i; int j;
        while (l <= r) {
            mid = (l + r) / 2;
            i = mid;
            j = k - i;
            if (j == 0 || arr1[i-1] > arr2[j-1]) {
                r = mid - 1;
                p = mid;
            }
            else {
                l = mid + 1;
            }
        }
        i = p;
        j = k - i;
        if (i != 0) {
            return Math.min(arr2[j], arr1[i-1]);
        }
        else {
            return arr2[j-1];
        }
    }

    public static void main(String [] args) {
        int [] arr1 = {1, 4, 5, 8};
        int [] arr2 = {2, 6, 10, 12};
        int k = 3;
        System.out.println(solution(arr1, arr2, 5));
    }
}
