package FatigueScore;

class Solution {
    static int answer = 0;
    static int [] visited;

    public static int solution(int k, int[][] dungeons) {
        visited = new int [dungeons.length];
        dfs(k, dungeons, 0);
        return answer;
    }

    public static void dfs(int k, int[][] dungeons, int depth) {
        for (int i=0;i < dungeons.length; i++) {
            int minimumStat = dungeons[i][0];
            int exhaust = dungeons[i][1];

            if (k >= minimumStat & visited[i] == 0) {
                visited[i] = 1;
                answer = Math.max(answer, depth+1);
                dfs(k-exhaust, dungeons, depth+1);
                visited[i] = 0;
            }
        }
    }

    public static void main(String [] args) {
        int k = 80;
        int [][] dungeons = {{80, 20}, {50, 40}, {30, 10}};
        solution(k, dungeons);
    }
}