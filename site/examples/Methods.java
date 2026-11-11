public class Methods {
    static int add(int a, int b) { return a + b; }
    static double add(double a, double b) { return a + b; }   // overload: same name, other types

    static long factorial(int n) {
        return n <= 1 ? 1 : n * factorial(n - 1);              // calls itself
    }

    public static void main(String[] args) {
        System.out.println(add(2, 3));
        System.out.println(add(2.5, 0.25));
        System.out.println("20! = " + factorial(20));
    }
}
