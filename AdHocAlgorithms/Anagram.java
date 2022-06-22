package AdHocAlgorithms;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

public class Anagram {
    public static int solution(String [] words) {
        ArrayList <String> arr = new ArrayList<>();
        for (String word : words) {
            StringBuilder sb = new StringBuilder("00000000000000000000000000");
            for (Character c : word.toCharArray()) {
                if (Character.isLowerCase(c)) {
                    int cnt = (sb.charAt((int)c - 97))-'0' + 1;
                    sb.replace((int)c - 97, (int)c - 97 + 1, String.valueOf(cnt));
                }
            }
            arr.add(sb.toString());
        }
        Collections.sort(arr);
        System.out.println(Arrays.toString(new ArrayList[]{arr}));

        int cnt = 1;
        int answer = 0;
        for (int i=0; i<arr.size()-1;i++) {
            if (arr.get(i).equals(arr.get(i+1))) cnt ++;
            else {
                answer += (cnt * (cnt - 1)) / 2;
                cnt = 1;
            }
        }
        answer += (cnt * (cnt - 1)) / 2;

        return answer;
    }

    public static void main(String [] args) {
        String [] words = {"purple", "plepur", "asdf", "dfsa", "fsad"};
        System.out.println(solution(words));
    }
}
