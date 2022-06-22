package TreeTrioMedian;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {

    public static int solution(int n, int[][] edges) {
        if (n == 3) return 1;
        ArrayList<Integer>[] adj_lst = new ArrayList[n];
        int[] indegree = new int[n];
        int[] children = new int[n];

        for (int i = 0; i < n; i++) {
            adj_lst[i] = new ArrayList<>();
        }

        for (int[] edge : edges) {
            int a = edge[0] - 1;
            int b = edge[1] - 1;
            indegree[a] += 1;
            indegree[b] += 1;
            adj_lst[a].add(b);
            adj_lst[b].add(a);
        }

        Queue<Integer> queue = new LinkedList<>();
        int[] visited = new int[n];
        for (int i = 0; i < n; i++) {
            if (indegree[i] == 1) {
                queue.add(i);
                visited[i] = 1;
            }
        }

        int distance = 0;
        ArrayList<Integer> center = new ArrayList<>();
        while (!queue.isEmpty()) {
            int curItems = queue.size();
            center.clear();
            center.addAll(queue);
            while (curItems > 0) {
                int x = queue.poll();
                for (int nx : adj_lst[x]) {
                    if (visited[nx] == 0) {
                        indegree[nx] -= 1;
                        if (indegree[nx] == 1) {
                            queue.add(nx);
                        }
                    }
                }
                curItems -= 1;
            }
            if (!queue.isEmpty()) distance += 1;
        }

        for (int i = 0; i < n; i++) {
            visited[i] = 0;
        }
        for (int c : center) {
            int child = 0;
            for (int nc : adj_lst[c]) {
                if (!center.contains(nc)) {
                    child += 1;
                }
            }
            children[c] = child;
        }

        queue.add(center.get(0));
        visited[center.get(0)] = 1;
        int[] d = new int[n];
        while (!queue.isEmpty()) {
            int x = queue.poll();
            for (int nx : adj_lst[x]) {
                if (visited[nx] == 0) {
                    queue.add(nx);
                    visited[nx] = 1;
                    d[nx] = d[x] + 1;
                }
            }
        }

        if (center.size() == 1) return 2 * distance;
        if (center.size() == 2) {
            if (children[center.get(1)] >= 2 || children[center.get(0)] >= 2) {
                return 2*distance + d[center.get(1)];
            }
            return 2*distance + d[center.get(1)] - 1;
        }
        if (children[center.get(1)] >= 2 || children[center.get(0)] >= 2) {
            return 2 * distance + Arrays.stream(d).max().getAsInt();
        }
        return 2 * distance + Arrays.stream(d).max().getAsInt() - 1;
    }


        public static void main (String[]args){
            int n = 6;
            int[][] edges = new int[][]{{1, 3}, {2, 3}, {3, 4}, {4, 5}, {4, 6}};
            System.out.println(solution(n, edges));
        }
    }


