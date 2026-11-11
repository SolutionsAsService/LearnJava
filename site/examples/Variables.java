public class Variables {
    public static void main(String[] args) {
        int age = 30;            // a 32-bit whole number
        double price = 4.50;     // a number with a fractional part
        boolean open = true;     // true or false, nothing else
        char grade = 'A';        // one character
        // long holds bigger whole numbers; _ only helps you read it
        long stars = 100_000_000_000L;
        var name = "Ada";        // the compiler works out: String

        System.out.println(name + " is " + age + ", grade " + grade);
        System.out.println("stars: " + stars + ", open: " + open);
        System.out.println("price: " + price);
        System.out.println("int is " + Integer.BYTES + " bytes, "
                + "long is " + Long.BYTES + " bytes");
        System.out.println("largest int: " + Integer.MAX_VALUE);
        // one past the largest int wraps around to the smallest
        System.out.println("largest int + 1: " + (Integer.MAX_VALUE + 1));
    }
}
