package GroupPhoto;

class Solution {
    private int answer = 0;
    private String[] friends = {"A", "C", "F", "J", "M", "N", "R", "T"};

    public int solution(int n, String[] data) {
        boolean[] isVisited = new boolean[8];
        dfs("", isVisited, data);
        return answer;
    }

    private void dfs(String names, boolean[] isVisited, String[] datas) {
        if (names.length() == 8) {
            if (check(names, datas)) {
                answer++;
            }
            return;
        }
        for (int i = 0; i < isVisited.length; i++) {
            if (!isVisited[i]) {
                isVisited[i] = true;
                dfs(names + friends[i], isVisited, datas);
                isVisited[i] = false;
            }
        }
    }


    private boolean check(String names, String[] datas) {
        for (String data : datas) {
            int position1 = names.indexOf(data.charAt(0));
            int position2 = names.indexOf(data.charAt(2));
            char op = data.charAt(3);
            int index = data.charAt(4) -'0';

            if (op == '>' && Math.abs(position1 - position2) - 1 > index) return true;
            else if (op == '=' && Math.abs(position1 - position2) - 1 == index) return true;
            else if (op == '<' && Math.abs(position1 - position2) - 1 < index) return true;
        }

        return false;
    }

}