import java.util.*;

public class CollectionsDemo {
    static <T extends Comparable<T>> T largest(List<T> items) {   // one method, any comparable type
        T best = items.get(0);
        for (T t : items) if (t.compareTo(best) > 0) best = t;
        return best;
    }

    public static void main(String[] args) {
        List<String> langs = new ArrayList<>(List.of("Java", "Kotlin", "Scala", "Groovy"));
        langs.add("Clojure");
        System.out.println(langs);

        Map<String, Integer> born = new TreeMap<>();               // sorted by key
        born.put("Java", 1996); born.put("Scala", 2004); born.put("Kotlin", 2016);
        System.out.println(born);

        Set<String> unique = new HashSet<>(List.of("a", "b", "a"));
        System.out.println("unique: " + unique.size());

        System.out.println("largest: " + largest(langs) + ", " + largest(List.of(3, 9, 4)));
    }
}
