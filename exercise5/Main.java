import java.util.Hashtable;

public class Main {
    public static void main(String[] args) {
        Integer n = Integer.parseInt(args[0]);
        System.out.println("Maldad: " + maldad(n));
    }

    public static Integer maldad(Integer n) {
        Integer k = (int) Math.floor(Math.log(n) / Math.log(2));
        Integer N = N(n, k);
        Integer trib = trib((int) Math.floor(Math.log(N) / Math.log(2) + 1), new Hashtable<Integer, Integer>());
        return trib;
    }

    public static Integer trib(Integer n, Hashtable<Integer, Integer> memo) {
        if (n <= 0) {
            return 0;
        } else if (n == 1 || n == 2) {
            return n;
        } else {
            if (memo.containsKey(n)) {
                return memo.get(n);
            }
            Integer n1, n2, n3;
            if (memo.containsKey(n - 1)) {
                n1 = memo.get(n - 1);
            } else {
                n1 = trib(n - 1, memo);
                memo.put(n - 1, n1);
            }
            if (memo.containsKey(n - 2)) {
                n2 = memo.get(n - 2);
            } else {
                n2 = trib(n - 2, memo);
                memo.put(n - 2, n2);
            }
            if (memo.containsKey(n - 3)) {
                n3 = memo.get(n - 3);
            } else {
                n3 = trib(n - 3, memo);
                memo.put(n - 3, n3);
            }
            return n1 + n2 + n3;
        }
    }

    public static Integer N(Integer n, Integer k) {
        return N(n, k, new Hashtable<String, Integer>());
    }

    public static Integer N(Integer n, Integer k, Hashtable<String, Integer> memo) {
        if (n == 0 && k == 0) {
            return 1;
        } else if (n == 0 && k != 0) {
            return 0;
        } else if (n < 0) {
            return 0;
        } else {
            if (memo.containsKey(n + "," + k)) {
                return memo.get(n + "," + k);
            }
            Integer n1, n2, n3;
            if (memo.containsKey((n - 1) + "," + (k - 1))) {
                n1 = memo.get((n - 1) + "," + (k - 1));
            } else {
                n1 = N(n - 1, k - 1, memo);
                memo.put((n - 1) + "," + (k - 1), n1);
            }
            if (memo.containsKey((n - 1) + "," + k)) {
                n2 = memo.get((n - 1) + "," + k);
            } else {
                n2 = N(n - 1, k, memo);
                memo.put((n - 1) + "," + k, n2);
            }
            if (memo.containsKey((n - 1) + "," + (k + 1))) {
                n3 = memo.get((n - 1) + "," + (k + 1));
            } else {
                n3 = N(n - 1, k + 1, memo);
                memo.put((n - 1) + "," + (k + 1), n3);
            }
            return n1 + n2 + n3;
        }
    }
}
