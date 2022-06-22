package AdHocAlgorithms;

import java.lang.reflect.Array;
import java.util.Arrays;

public class gap {
    static int [] arr = {1, 4, 6, 9, 13, 18, 33, 35, 39};
    static int M = 100;

    public static int [] query(int x, int y) {
        int [] ans = {-1, -1};
        for (int i=0; i<arr.length; i++){
            if (arr[i] <= y && arr[i] >= x) {
                ans[0] = arr[i];
                break;
            }
        }
        for (int i=arr.length-1; i>=0; i--){
            if (x <= arr[i] && arr[i] <= y) {
                ans[1] = arr[i];
                break;
            }
        }
        return ans;
    }

    public static int solution() {
        int min; int max;
        int [] t;
        t = query(1, M);
        min = t[0]; max = t[1];
        int interval = (max-min)/(arr.length+1);
        int answer = -1;
        for (int i=min+1; i<max-1; i+=interval) {
            t = query(i, i+(max-min)/(arr.length-1));
            if (t[0] != -1) answer = Math.max(t[0]-min, answer);
            if (t[1] != -1) min = t[1];
        }
        answer = Math.max(answer, max-t[1]);

        return answer;
    }

    public static void main(String [] args) {
        System.out.println(solution());
    }
}
