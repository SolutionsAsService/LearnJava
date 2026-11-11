import java.util.Arrays;

public class ArraysDemo {
    public static void main(String[] args) {
        int[] scores = {72, 95, 88, 61};
        System.out.println("length: " + scores.length);

        int total = 0;
        for (int s : scores) total += s;          // the enhanced for loop
        System.out.println("total: " + total);

        Arrays.sort(scores);
        System.out.println("sorted: " + Arrays.toString(scores));

        try {
            System.out.println(scores[4]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("checked at run time: " + e.getMessage());
        }
    }
}
