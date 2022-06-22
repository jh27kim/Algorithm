package Camping;


import java.util.*;


/*
class Solution {
    public static int solution(int n, int[][] data) {
        int answer = 0;
        HashMap<Integer, ArrayList<Integer>> ROW_DICT = new HashMap<>();
        HashMap<Integer, ArrayList<Integer>> COL_DICT = new HashMap<>();

        Arrays.sort(data, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] > o2[0]) return 1;
                if (o1[0] == o2[0] & o1[1] > o2[1]) return 1;
                return -1;
            }
        });

        System.out.println(Arrays.deepToString(data));

        for (int [] dots : data) {
            int x = dots[0]; int y = dots[1];
            if (ROW_DICT.get(x) == null) {
                ROW_DICT.put(x, new ArrayList<>());
            }
            if (COL_DICT.get(y) == null) {
                COL_DICT.put(y, new ArrayList<>());
            }
            //System.out.println((char)(x+'0') + ", " + (char)(y+'0'));
            ROW_DICT.get(x).add(y);
            COL_DICT.get(y).add(x);

            //test(ROW_DICT);
            //System.out.println();
        }


        for (int i = 0; i < n; i++) {
            int pivotX = data[i][0];
            int pivotY = data[i][1];
            for (int j = i + 1; j < n; j++) {
                int varX = data[j][0];
                int varY = data[j][1];
                if (varX == pivotX | varY == pivotY) continue;
                int r = ROW_DICT.get(varX).size() - ROW_DICT.get(varX).indexOf(varY);
                int c= COL_DICT.get(varY).size() - COL_DICT.get(varY).indexOf(varX);
                //System.out.println((char)(pivotX+'0') + ", " + (char)(pivotY+'0') + " : " + (char)(varX+'0') + ", " + (char)(varY+'0'));
                answer += (r+c-1);
                //System.out.println((char)(r+'0') + ", " + (char)(c+'0'));
                break;
            }
        }
        //System.out.println(answer);
        return answer;
    }

    public static void main(String [] args){
        int n = 4;
        int [][] data = new int [][]{{0, 0}, {1, 1}, {0, 2}, {2, 0}};
        solution(n, data);
    }

    public static void test(HashMap<Integer, ArrayList<Integer>> ROW_DICT) {
        Iterator<Map.Entry<Integer, ArrayList<Integer>>> iter = ROW_DICT.entrySet().iterator();
        while (iter.hasNext()) {
            Map.Entry<Integer, ArrayList<Integer>> entry = iter.next();
            System.out.println("Key = " + entry.getKey() + ", Value = " + entry.getValue());
        }
    }
}
*/

class Solution {
    public static int solution(int n, int[][] data) {
        HashSet <Integer> distinctX = new HashSet<>();
        HashSet <Integer> distinctY = new HashSet<>();
        int [][] dp = new int [5000][5000];
        int answer = 0;

        for (int [] d : data) {
            distinctX.add(d[0]);
            distinctY.add(d[1]);
        }

        ArrayList <Integer> pointX = new ArrayList<>(distinctX);
        ArrayList <Integer> pointY = new ArrayList<>(distinctY);

        Collections.sort(pointX);
        Collections.sort(pointY);

        for (int i=0; i<n; i++) {
            data[i][0] = pointX.indexOf(data[i][0]);
            data[i][1] = pointY.indexOf(data[i][1]);
            dp[data[i][0]][data[i][1]] = 1;
        }

        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                dp[i][j] += (i-1 > -1? dp[i-1][j] : 0) + (j-1 > -1 ? dp[i][j-1] : 0)
                        - ((i-1 > -1 & j-1 > -1) ? dp[i-1][j-1] : 0);
            }
        }

        for (int i=0; i<n; i++) {
            for (int j=i+1; j<n; j++) {
                if (data[i][0] == data[j][0] | data[i][1] == data[j][1]) continue;
                int cnt = 0;
                int startX = data[i][0] < data[j][0] ? data[i][0] : data[j][0];
                int startY = data[i][1] < data[j][1] ? data[i][1] : data[j][1];
                int endX = data[i][0] > data[j][0] ? data[i][0] : data[j][0];
                int endY = data[i][1] > data[j][1] ? data[i][1] : data[j][1];

                if (startX + 1 > endX - 1 || startY + 1 > endY - 1) {
                    cnt = 0;
                }

                else {
                    cnt = dp[endX-1][endY-1] - dp[endX-1][startY] - dp[startX][endY-1]
                    + dp[startX][startY];
                }
                if (cnt == 0) answer ++;
            }
        }
        return answer;
    }

    public static void main(String [] args){
        int n = 4;
        int [][] data = new int [][]{{0, 0}, {1, 1}, {0, 2}, {2, 0}};

        System.out.println(solution(n, data));
    }
}





















































