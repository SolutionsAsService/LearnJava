import java.io.*;
import java.nio.file.*;

public class Exceptions {
    static int parse(String s) {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {          // unchecked: the compiler does not insist
            System.out.println("not a number: " + s);
            return 0;
        } finally {
            System.out.println("parsed " + s);       // runs either way
        }
    }

    public static void main(String[] args) throws IOException {   // checked: must be declared or caught
        System.out.println(parse("42") + parse("x"));

        Path file = Files.createTempFile("learnjava", ".txt");
        Files.writeString(file, "one\ntwo\n");
        try (BufferedReader in = Files.newBufferedReader(file)) {   // closed automatically
            System.out.println("first line: " + in.readLine());
        }
        Files.delete(file);
    }
}
