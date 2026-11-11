public class Records {
    // sealed: these three are the only shapes there will ever be
    sealed interface Shape permits Circle, Square, Rect {}
    record Circle(double r) implements Shape {}
    record Square(double side) implements Shape {}
    record Rect(double w, double h) implements Shape {}

    // no default: the compiler knows every case is covered
    static double area(Shape s) {
        return switch (s) {
            case Circle c -> Math.PI * c.r() * c.r();
            case Square q -> q.side() * q.side();
            case Rect(double w, double h) -> w * h;
        };
    }

    public static void main(String[] args) {
        Shape[] shapes = { new Circle(1), new Square(2), new Rect(2, 3) };
        for (Shape s : shapes) {
            System.out.printf("%s -> %.2f%n", s, area(s));
        }
        // records compare by value
        System.out.println(new Square(2).equals(new Square(2)));
    }
}
