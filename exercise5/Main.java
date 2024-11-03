import java.util.Hashtable;
import java.lang.Math;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) {
        try {
            // Check if the number of arguments is correct
            if (args.length != 1) {
                throw new Exception("Usage: java Main <n>");
            }

            // Parse the argument
            Integer n = Integer.parseInt(args[0]);
            System.out.println("Maldad: " + maldad(n));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    /**
     * Calculates the maldad of a number n
     * @param n number
     * @return maldad de n
     */
    public static BigInteger maldad(Integer n) {
        // k = log2(n)
        Integer k = (int) Math.floor(Math.log(n) / Math.log(2));
        // N(n, k) - Narayana number
        BigInteger N = N(n, k);
        // trib(N) - Tribonacci number
        BigInteger trib = trib(BigInteger.valueOf((int) Math.floor(Math.log(N.doubleValue()) / Math.log(2)) + 1), new Hashtable<BigInteger, BigInteger>());
        return trib;
    }

    /**
     * Calculates the tribonacci number of n
     * @param n number
     * @param memo memoization table
     * @return tribonacci number of n
     */
    public static BigInteger trib(BigInteger n, Hashtable<BigInteger, BigInteger> memo) {
        // trib(n) = n if 0 <= n <= 2
        if (n.compareTo(BigInteger.ZERO) >= 0 && n.compareTo(BigInteger.TWO) <= 0) {
            return n;
        // trib(n) = trib(n - 1) + trib(n - 2) + trib(n - 3)
        } else {
            // If the value is already calculated, return it
            if (memo.containsKey(n)) {
                return memo.get(n);
            }
            // Check if the values of trib(n - 1), trib(n - 2) and trib(n - 3) are already calculated. If not, calculate them
            BigInteger n1, n2, n3;

            // n1 = trib(n - 1)
            if (memo.containsKey(n.subtract(BigInteger.ONE))) {
                n1 = memo.get(n.subtract(BigInteger.ONE));
            } else {
                n1 = trib(n.subtract(BigInteger.ONE), memo);
                memo.put(n.subtract(BigInteger.ONE), n1);
            }

            // n2 = trib(n - 2)
            if (memo.containsKey(n.subtract(BigInteger.TWO))) {
                n2 = memo.get(n.subtract(BigInteger.TWO));
            } else {
                n2 = trib(n.subtract(BigInteger.TWO), memo);
                memo.put(n.subtract(BigInteger.TWO), n2);
            }

            // n3 = trib(n - 3)
            if (memo.containsKey(n.subtract(BigInteger.valueOf(3)))) {
                n3 = memo.get(n.subtract(BigInteger.valueOf(3)));
            } else {
                n3 = trib(n.subtract(BigInteger.valueOf(3)), memo);
                memo.put(n.subtract(BigInteger.valueOf(3)), n3);
            }

            return n1.add(n2).add(n3);
        }
    }

    /**
     * Calculates the Narayana number of n and k
     * @param n number
     * @param k number
     * @return Narayana number of n and k
     */
    public static BigInteger N(Integer n, Integer k) {
        // Call the recursive function with the memoization table
        Hashtable<String, BigInteger> memo = new Hashtable<String, BigInteger>();
        return binomial(n, k, memo).multiply(binomial(n, k - 1, memo)).divide(BigInteger.valueOf(n));
    }

    public static BigInteger binomial(Integer n, Integer k, Hashtable<String, BigInteger> memo) {
        // binomial(n, k) = 1 if k = 0 or k = n
        if (k == 0 || k == n) {
            return BigInteger.ONE;
        // binomial(n, k) = binomial(n - 1, k - 1) + binomial(n - 1, k)
        } else {
            // If the value is already calculated, return it
            String key = n + "," + k;
            if (memo.containsKey(key)) {
                return memo.get(key);
            }
            // Check if the values of binomial(n - 1, k - 1) and binomial(n - 1, k) are already calculated. If not, calculate them
            BigInteger n1, n2;

            // n1 = binomial(n - 1, k - 1)
            if (memo.containsKey((n - 1) + "," + (k - 1))) {
                n1 = memo.get((n - 1) + "," + (k - 1));
            } else {
                n1 = binomial(n - 1, k - 1, memo);
                memo.put((n - 1) + "," + (k - 1), n1);
            }

            // n2 = binomial(n - 1, k)
            if (memo.containsKey((n - 1) + "," + k)) {
                n2 = memo.get((n - 1) + "," + k);
            } else {
                n2 = binomial(n - 1, k, memo);
                memo.put((n - 1) + "," + k, n2);
            }

            return n1.add(n2);
        }
    }
}
