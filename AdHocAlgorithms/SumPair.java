package AdHocAlgorithms;

import java.util.Arrays;

public class SumPair {
    public static int solution(int [] arr1, int [] arr2, int n) {
        Arrays.sort(arr1);
        Arrays.sort(arr2);
        int i = 0;
        int j = arr2.length-1;

        int answer = 0;
        while (i < arr1.length & j >= 0) {
            if (arr1[i] + arr2[j] < n) i++;
            else if (arr1[i] + arr2[j] > n) j--;
            else {
                answer ++;
                if (i+1 < arr1.length) i++;
                else j--;
            }
        }
        return answer;
    }

    public static void main(String [] args) {
        int [] arr1 = {5, 2, 6, 8, 1, 10};
        int [] arr2 = {11, 9, 3, 7, 4, 12};
        System.out.println(solution(arr1, arr2, 12));
    }
}
