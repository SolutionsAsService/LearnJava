public class Strings {
    public static void main(String[] args) {
        String a = "java";
        String b = new String("java");
        System.out.println("a == b: " + (a == b));            // same object? no
        System.out.println("a.equals(b): " + a.equals(b));    // same text? yes

        String upper = a.toUpperCase();                      // a new string; a is unchanged
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
