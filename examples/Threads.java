import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicInteger;

public class Threads {
    public static void main(String[] args) {
        AtomicInteger done = new AtomicInteger();
        // Java 21: a new, cheap virtual thread for every task
        try (var pool = Executors.newVirtualThreadPerTaskExecutor()) {
            for (int i = 0; i < 10_000; i++) {
                pool.submit(() -> {
                    Thread.sleep(10);  // blocks only this thread
                    return done.incrementAndGet();
                });
            }
        }  // leaving the block waits for every task
        System.out.println("tasks finished: " + done.get());
    }
}
