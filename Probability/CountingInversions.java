package Probability;

import java.util.Arrays;

public class CountingInversions {
    private static int merge(int [] arr, int l, int m, int r) {
        int [] left = Arrays.copyOfRange(arr, l, m+1);
        int [] right = Arrays.copyOfRange(arr, m+1, r+1);

        int i = 0, j = 0, k = l, swaps = 0;

        while (i < left.length && j < right.length) {
            if (left[i] <= right[j])
                arr[k++] = left[i++];
            else {
                arr[k++] = right[j++];
                swaps += (m + 1) - (l + i);
            }
        }
        while (i < left.length)
            arr[k++] = left[i++];
        while (j < right.length)
            arr[k++] = right[j++];
        return swaps;
    }

    public static int solution(int [] arr, int l, int r) {

        int count = 0;
        if (l < r) {
            int m = (l + r)/2;
            count += solution(arr, l, m);
            count += solution(arr, m+1, r);
            count += merge(arr, l, m, r);
        }
        return count;
    }

    public static void main(String [] args) {
        int [] arr = {1, 20, 6, 4, 5};
        System.out.println(solution(arr, 0, arr.length-1));
        System.out.println(Arrays.toString(arr));
    }
}
