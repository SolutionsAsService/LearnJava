public class Classes {
    static class Account {
        private final String owner;   // set once, in the constructor
        private long cents;            // private: only Account can change it

        Account(String owner) { this.owner = owner; }

        void deposit(long amount) {
            if (amount <= 0) throw new IllegalArgumentException("amount must be positive");
            cents += amount;
        }

        @Override
        public String toString() { return owner + ": " + cents / 100 + "." + String.format("%02d", cents % 100); }
    }

    public static void main(String[] args) {
        Account a = new Account("Ada");
        a.deposit(1050);
        a.deposit(25);
        System.out.println(a);
    }
}
