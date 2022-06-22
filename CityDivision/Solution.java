package CityDivision;

import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution {
    private static class Edge implements Comparable<Edge> {
        private int from;
        private int to;
        private int cost;

        Edge(int a, int b, int c) {
            from = a;
            to = b;
            cost = c;
        }

        @Override
        public int compareTo(Edge e1) {
            return this.cost - e1.cost;
        }

        @Override
        public String toString() {
            return "From: " + String.valueOf(this.from) + "  To: " + String.valueOf(this.to) + "  Cost: " +  String.valueOf(this.cost);
        }
    }

    public static int find(int x, int [] parents) {
        if (x != parents[x]) {
            parents[x] = find(parents[x], parents);
        }
        return parents[x];
    }

    public static void union(int x, int y, int[] parents) {
        int a = find(x, parents);
        int b = find(y, parents);
        if (a < b) {
            parents[a] = b;
        }
        else parents[b] = a;
    }

    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        PriorityQueue <Edge> minHeap = new PriorityQueue<Edge>();

        for (int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            minHeap.add(new Edge(a, b, c));
        }

        int edges = 0;
        int answer = 0;
        int [] parents = new int[N+1];
        for (int i=1; i<N+1; i++) {
            parents[i] = i;
        }

        while (edges != N-2) {
            Edge curEdge = minHeap.poll();
            int x = curEdge.from;
            int y = curEdge.to;
            int cost = curEdge.cost;

            if (find(x, parents) != find(y, parents)) {
                union(x, y, parents);
                answer += cost;
                edges += 1;
            }
        }
        System.out.println(answer);
    }
}
