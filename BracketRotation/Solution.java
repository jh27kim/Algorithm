package BracketRotation;

import java.util.LinkedList;

class Solution {
    public static int solution(String s) {
        StringBuilder sb = new StringBuilder(s);
        int answer = 0;
        for (int i=0; i<s.length(); i++) {
            if (check(sb.substring(i, i+s.length()))) {
                answer += 1;
            }

            sb.append(sb.charAt(i));
        }
        return answer;
    }

    public static boolean check(String substring) {
        LinkedList <Character> stack = new LinkedList <>();
        char c;

        for (int i=0; i<substring.length(); i++) {
            c = substring.charAt(i);
            if (stack.isEmpty()) {
                stack.add(c);
                continue;
            }
            if ((stack.getLast() == '[' && c == ']') || (stack.getLast() == '{' && c == '}') || (stack.getLast() == '(' && c == ')')) {
                stack.removeLast();
            }
            else {
                stack.add(c);
            }
        }
        return stack.isEmpty();
    }

    public static void main (String [] args) {
        String s = "{}]()[";
        solution(s);
    }

}