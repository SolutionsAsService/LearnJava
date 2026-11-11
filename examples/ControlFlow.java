public class ControlFlow {
    public static void main(String[] args) {
        int temperature = 18;
        if (temperature > 25) {
            System.out.println("hot");
        } else if (temperature > 15) {
            System.out.println("mild");
        } else {
            System.out.println("cold");
        }

        String day = "SAT";
        String kind = switch (day) {         // a switch expression returns a value
            case "SAT", "SUN" -> "weekend";
            default -> "weekday";
        };
        System.out.println(day + " is a " + kind);

        int n = 27, steps = 0;
        while (n != 1) {
            n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
            steps++;
        }
        System.out.println("27 reaches 1 in " + steps + " steps");
    }
}
