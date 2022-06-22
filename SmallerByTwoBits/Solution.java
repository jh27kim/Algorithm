package SmallerByTwoBits;

class Solution {

    public static long[] solution(long[] numbers) {
        long[] answer = new long [numbers.length];
        for (int i=0; i<numbers.length; i++) {
            answer[i] = f(numbers[i]);
        }
        return answer;
    }

    public static long f(long number) {


        if (number % 2 == 0) {
            return number + 1;
        }
        else {
            StringBuilder temp = new StringBuilder();
            String binaryString = Long.toBinaryString(number);
            if (binaryString.contains("0")) {
                int lastZero = binaryString.lastIndexOf("0");
                int firstOneAfterLastZero = binaryString.indexOf("1", lastZero);

                temp.append(binaryString, 0, lastZero).append("1");
                temp.append("0");
                temp.append(binaryString.substring(firstOneAfterLastZero+1));
            }
            else {
                temp.append("10");
                temp.append(binaryString.substring(1).replace("0", "1"));
            }
            return Long.parseLong(temp.toString(), 2);
        }
    }

    public static void main(String [] args) {
        long[] numbers = {2, 7};
        solution(numbers);
    }

}