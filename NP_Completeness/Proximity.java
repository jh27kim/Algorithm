package NP_Completeness;

public class Proximity {
    public static int solution(int [] offset, int [] ki, int k) {
        int answer = 1000;
        int i = 0; int j = 0;
        int totalCount = 0;
        int [] cnt = {0, 0, 0, 0};

        while (j < ki.length) {
            if (cnt[ki[j]] == 0) totalCount++;
            cnt[ki[j]] ++;

            while (totalCount == k && i < j) {
                answer = Math.min(answer, offset[j]-offset[i]+1);
                cnt[ki[i]] --;
                if (cnt[ki[i]] == 0) totalCount --;
                i ++;
            }
            j ++;
        }

        return answer;
    }

    public static void main(String [] args) {
        int [] offset = {0, 4, 5, 6, 9, 10, 12};
        int [] ki = {1, 3, 1, 1, 1, 2, 2};
        int k = 3;

        System.out.println(solution(offset, ki, 3));
    }
}
