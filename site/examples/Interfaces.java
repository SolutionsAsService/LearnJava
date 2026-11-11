import java.util.List;

public class Interfaces {
    interface Shape { double area(); }                  // a contract, no body

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
            System.out.printf("%s %.2f%n", s.getClass().getSimpleName(), s.area());  // decided at run time
        }
    }
}
