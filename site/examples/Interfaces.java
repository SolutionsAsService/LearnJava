import java.util.List;

public class Interfaces {
    // a contract: methods without bodies
    interface Shape { double area(); }

    static class Square implements Shape {
        final double side;
        Square(double side) { this.side = side; }
        public double area() { return side * side; }
    }

    static class Circle implements Shape {
        final double r;
        Circle(double r) { this.r = r; }
        public double area() { return Math.PI * r * r; }
    }

    public static void main(String[] args) {
        List<Shape> shapes = List.of(new Square(2), new Circle(1));
        for (Shape s : shapes) {
            // which area() runs is decided at run time
            String name = s.getClass().getSimpleName();
            System.out.printf("%s %.2f%n", name, s.area());
        }
    }
}
