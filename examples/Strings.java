public class Strings {
    public static void main(String[] args) {
        String a = "java";
        String b = new String("java");
        // == asks: the same object? equals asks: the same text?
        System.out.println("a == b: " + (a == b));
        System.out.println("a.equals(b): " + a.equals(b));

        // strings never change; toUpperCase makes a new one
        String upper = a.toUpperCase();
        System.out.println(a + " -> " + upper);

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= 3; i++) sb.append(i).append(' ');
        System.out.println(sb.toString().trim());

        String block = """
            A text block keeps
            its line breaks.""";
        System.out.println(block);
    }
}
