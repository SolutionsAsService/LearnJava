public class Variables {
    public static void main(String[] args) {
        int age = 30;               // 32-bit whole number
        long stars = 100_000_000_000L; // 64-bit; underscores are just for reading
        double price = 4.50;        // 64-bit floating point
        boolean open = true;        // true or false, nothing else
        char grade = 'A';           // one UTF-16 code unit
        var name = "Ada";           // the compiler infers String

        System.out.println(name + " is " + age + ", grade " + grade);
        System.out.println("stars: " + stars + ", open: " + open + ", price: " + price);
        System.out.println("int is " + Integer.BYTES + " bytes, long is " + Long.BYTES + " bytes");
        System.out.println("largest int: " + Integer.MAX_VALUE);
        System.out.println("largest int + 1: " + (Integer.MAX_VALUE + 1)); // wraps around
    }
}
