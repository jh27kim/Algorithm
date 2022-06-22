package KakaoFriendsSketchBook;
import java.util.LinkedList;
import java.util.Arrays;

class Solution {
    public static int [][] MOVEMENT = new int[][] {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public static int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;
        int [][] visited = new int[m][n];

        LinkedList <Integer []> queue = new LinkedList<>();

        for(int i=0; i<m; i++) {
            for(int j=0; j<n; j++) {
                if (picture[i][j] != 0 && visited[i][j] == 0) {
                    queue.add(new Integer []{i, j});
                    int [] args = new int []{m, n, picture[i][j]};
                    visited[i][j] = 1;
                    maxSizeOfOneArea = Math.max(maxSizeOfOneArea, bfs(queue, visited, args, picture));
                    numberOfArea += 1;
                }
            }
        }
        /*
        for(int i = 0; i < queue.size(); i++)
            System.out.println( Arrays.toString(queue.get(i)) );
         */

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        System.out.println(Arrays.toString(answer));
        return answer;
    }

    public static int bfs(LinkedList <Integer []> queue, int[][] visited, int [] args, int [][] picture) {
        int m  = args[0]; int n = args[1]; int c = args[2];
        int x; int y;
        int nx; int ny;
        int area = 1;

        while (!queue.isEmpty()) {
            Integer [] top = queue.pop();
            x = top[0]; y = top[1];
            //System.out.println(Arrays.toString(top));
            for (int [] move : MOVEMENT) {
                nx = x + move[0];
                ny = y + move[1];
                if (0 <= nx && nx < m && ny >= 0 && ny < n) {
                    if (visited[nx][ny] == 0 && picture[nx][ny] == c){
                        visited[nx][ny] = 1;
                        queue.add(new Integer[]{nx, ny});
                        area += 1;
                    }
                }
            }
        }

        return area;
    }

    public static void main(String [] args) {
        Solution s = new Solution();
        int m = 6;
        int n = 4;
        int [][] pictures = new int [][] {{1, 1, 1, 0},
                                          {1, 2, 2, 0},
                                          {1, 0, 0, 1},
                                          {0, 0, 0, 1},
                                          {0, 0, 0, 3},
                                          {0, 0, 0, 3}};
        Solution.solution(m, n, pictures);
    }
}