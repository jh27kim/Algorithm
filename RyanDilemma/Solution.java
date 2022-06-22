package RyanDilemma;

import java.util.*;

class Solution {
    static int START = 0;
    static int END = 1;

    public static int solution(int n, int m, int[][] timetable) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<int[]>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] > o2[0]) return 1;
                if ((o1[0] == o2[0]) & (o1[1] > o2[1])) return 1;
                return -1;
            }
        });

        for (int[] time : timetable) {
            int start = time[START];
            int end = time[END];
            minHeap.add(new int[]{start, START});
            minHeap.add(new int[]{end, END});
        }

        int temp = 0;
        int guests = 0;
        while (!minHeap.isEmpty()) {
            int[] arr = minHeap.poll();
            if (arr[1] == START) {
                temp += 1;
                guests = Math.max(guests, temp);
            } else temp -= 1;
        }

        if (guests == 1) return 0;
        for (int dis = 2 * n - 2; dis > 0; dis--) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    HashSet<int[]> pair = new HashSet<>();
                    pair.add(new int[]{i, j});
                    int curGuest = 1;
                    for (int y = i; y < n; y++) {
                        for (int x = 0; x < n; x++) {
                            if ((y < i) | (y == i & x <= j)) continue;
                            Iterator<int[]> iter = pair.iterator();
                            while (iter.hasNext()) {
                                int[] nxt = iter.next();
                                int d = Math.abs(y - nxt[0]) + Math.abs(x - nxt[1]);
                                if (d < dis) break;
                            }
                            if (iter.next() != null) {
                                pair.add(new int[]{y, x});
                                curGuest += 1;
                            }
                            if (curGuest == guests) {
                                return dis;
                            }
                        }
                    }
                }
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        int n = 2;
        int m = 2;
        int [][] timetable = {{600, 630}, {630, 700}};
        System.out.println(solution(n, m, timetable));
    }

    public static void check(PriorityQueue <int []> arr) {
        while (!arr.isEmpty()) {
            System.out.println(Arrays.toString(arr.poll()));
        }
    }
}