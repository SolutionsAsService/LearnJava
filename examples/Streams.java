import java.util.List;
import java.util.stream.Collectors;

public class Streams {
    record Lang(String name, int year) {}

    public static void main(String[] args) {
        List<Lang> jvm = List.of(new Lang("Java", 1996), new Lang("Groovy", 2003),
                                 new Lang("Scala", 2004), new Lang("Clojure", 2007), new Lang("Kotlin", 2016));

        String after2000 = jvm.stream()
            .filter(l -> l.year() > 2000)               // a lambda: a function written in place
            .map(Lang::name)                            // a method reference
            .sorted()
            .collect(Collectors.joining(", "));
        System.out.println(after2000);

        int total = jvm.stream().mapToInt(Lang::year).sum();
        System.out.println("average year: " + total / jvm.size());
    }
}
