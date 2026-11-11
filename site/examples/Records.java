public class Records {
    sealed interface Shape permits Circle, Square, Rect {}   // the only three shapes there will ever be
    record Circle(double r) implements Shape {}
    record Square(double side) implements Shape {}
    record Rect(double w, double h) implements Shape {}

    static double area(Shape s) {
        return switch (s) {                                  // no default needed: the compiler knows all cases
            case Circle c -> Math.PI * c.r() * c.r();
            case Square q -> q.side() * q.side();
            case Rect(double w, double h) -> w * h;          // record pattern: unpack in place
        };
    }

    public static void main(String[] args) {
        Shape[] shapes = { new Circle(1), new Square(2), new Rect(2, 3) };
        for (Shape s : shapes) System.out.printf("%s -> %.2f%n", s, area(s));
        System.out.println(new Square(2).equals(new Square(2)));  // records compare by value
    }
}
