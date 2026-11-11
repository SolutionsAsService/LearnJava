import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class Threads {
    public static void main(String[] args) {
        AtomicInteger done = new AtomicInteger();
        try (var pool = Executors.newVirtualThreadPerTaskExecutor()) {   // Java 21: one cheap thread per task
            for (int i = 0; i < 10_000; i++) {
                pool.submit(() -> {
                    Thread.sleep(10);                                       // blocks only this virtual thread
                    return done.incrementAndGet();
                });
            }
        }                                                                   // waits for every task
        System.out.println("tasks finished: " + done.get());
    }
}
