package AdHocAlgorithms;

public class SingleItem {
    public static void main(String [] args) {
        int [] arr = {3, 3, 8, 8, 5, 5, 10, 10, 7, 7, 2, 14, 14};
        int answer = arr[0];
        for (int i=1; i<arr.length; i++) {
            answer ^= arr[i];
        }
        System.out.println(answer);
    }
}
