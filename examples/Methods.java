public class Methods {
    static int add(int a, int b) { return a + b; }

    // an overload: the same name, other parameter types
    static double add(double a, double b) { return a + b; }

    // a method that calls itself
    static long factorial(int n) {
        return n <= 1 ? 1 : n * factorial(n - 1);
    }

    public static void main(String[] args) {
        System.out.println(add(2, 3));
        System.out.println(add(2.5, 0.25));
        System.out.println("20! = " + factorial(20));
    }
}
