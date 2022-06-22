package LightPathCycle;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    static Node [][] board;
    static int [][] MOVEMENT = new int [][] {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
    static int INBOUND = 0;
    static int OUTBOUND = 1;

    static class Node {
        int [][] visited;
        char block;

        public Node (char c) {
            this.block = c;
            //////////////////////// {UP, RIGHT, DOWN, LEFT} ////////////////////////
            //////////////////////// {INBOUND, OUTBOUND} ////////////////////////
            this.visited = new int[][]{{0, 0}, {0, 0}, {0, 0}, {0, 0}};
        }

        @Override
        public String toString() {
            String ret = "";
            for (int [] v : this.visited) {
                for (int c : v) {
                    ret += (char)(c + '0') + ":";
                }
                ret += "  ";
            }
            return ret;
        }
    }

    static class Light {
        int x;
        int y;
        int dir;

        public Light(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.dir = d;
        }
    }

    public static int track(Light light, int distance) {
        while (true) {
            int curX = light.x;
            int curY = light.y;
            //System.out.println(Integer.toString(curX) + " ," + Integer.toString(curY)+ " :" + Integer.toString(light.dir));
            //System.out.println(board[curX][curY]);
            //System.out.println();

            Node curNode = board[curX][curY];
            int curDirection = light.dir;

            if (curNode.visited[(curDirection+2)%4][INBOUND] == 1) {
                //System.out.println("Returned");
                //System.out.println();
                break;
            }
            //Light direction -> Node direction
            curNode.visited[(curDirection+2)%4][INBOUND] = 1;

            //Direction update
            int nextDirection = 0;
            int newX = 0;
            int newY = 0;

            if (curNode.block == 'S') {
                nextDirection = curDirection;
            }

            else if (curNode.block == 'L') {
                nextDirection = (curDirection+1)%4;
            }

            else if (curNode.block == 'R') {
                nextDirection = curDirection - 1 < 0 ? 3 : curDirection - 1;
            }

            //Adjust cursor
            newX = (curX + MOVEMENT[nextDirection][0]) % board.length;
            newY = (curY + MOVEMENT[nextDirection][1]) % board[0].length;
            newX = newX < 0 ? board.length-1 : newX;
            newY = newY < 0 ? board[0].length-1 : newY;

            //Apply
            light.x = newX;
            light.y = newY;
            light.dir = nextDirection;
            curNode.visited[nextDirection][OUTBOUND] = 1;
            distance += 1;
        }
        return distance;
    }

    public static int[] solution(String[] grid) {
        ArrayList <Integer> answer = new ArrayList<>();
        board = new Node[grid.length][grid[0].length()];

        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                board[i][j] = new Node(grid[i].charAt(j));
            }
        }
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                for (int d=0; d<4; d++) {
                    if (board[i][j].visited[(d+2)%4][0] == 0) {
                        answer.add(track(new Light(i, j, d), 0));
                    }
                }
            }
        }
        Collections.sort(answer);
        int [] res = new int [answer.size()];
        for (int _i=0; _i < answer.size(); _i++) {
            res[_i] = answer.get(_i);
        }
        System.out.println(Arrays.toString(res));
        return res;
    }


    public static void main(String [] args) {
        String [] grid = {"R","R"};
        solution(grid);
    }
}