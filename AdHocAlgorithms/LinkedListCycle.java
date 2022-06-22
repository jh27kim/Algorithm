package AdHocAlgorithms;

public class LinkedListCycle {
    static class Node{
        int value;
        Node next;

        public Node(int value, Node next) {
            this.value = value;
            this.next = next;
        }
    }

    public static boolean solution() {
        Node n1 = new Node(1, null);
        Node n2 = new Node(2, null);
        Node n3 = new Node(3, null);
        Node n4 = new Node(4, null);
        n1.next = n2;
        n2.next = n3;
        n3.next = n4;
        n4.next = n1;

        Node i = n1;
        Node j = n2;
        while (true) {
            if (i.value == j.value) {
                return true;
            }
            i = i.next;
            j = j.next;
            j = j.next;
            System.out.println(i.value);
            System.out.println(j.value);
        }
    }

    public static void main(String [] args) {
        System.out.println(solution());
    }
}
