class Solution {
    // memo[i1][i2][len] = -1 unknown, 0 false, 1 true
    private int[][][] memo;
    private String s1, s2;

    public boolean isScramble(String s1, String s2) {
        int n = s1.length();
        if (n != s2.length()) return false;
        this.s1 = s1;
        this.s2 = s2;
        memo = new int[n][n][n + 1];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                for (int k = 0; k <= n; k++)
                    memo[i][j][k] = -1;

        return isScrambleRec(0, 0, n);
    }

    private boolean isScrambleRec(int i1, int i2, int len) {
        if (memo[i1][i2][len] != -1) return memo[i1][i2][len] == 1;

        // If substrings are exactly equal
        if (s1.regionMatches(i1, s2, i2, len)) {
            memo[i1][i2][len] = 1;
            return true;
        }

        // Quick prune: character frequency must match
        if (!sameCharCounts(i1, i2, len)) {
            memo[i1][i2][len] = 0;
            return false;
        }

        // Try every split
        for (int split = 1; split < len; split++) {
            // case 1: no swap
            if (isScrambleRec(i1, i2, split) && isScrambleRec(i1 + split, i2 + split, len - split)) {
                memo[i1][i2][len] = 1;
                return true;
            }

            // case 2: swap
            if (isScrambleRec(i1, i2 + len - split, split) && isScrambleRec(i1 + split, i2, len - split)) {
                memo[i1][i2][len] = 1;
                return true;
            }
        }

        memo[i1][i2][len] = 0;
        return false;
    }

    // Compare character counts for s1[i1..i1+len-1] and s2[i2..i2+len-1]
    private boolean sameCharCounts(int i1, int i2, int len) {
        int[] cnt = new int[26];
        for (int k = 0; k < len; k++) {
            cnt[s1.charAt(i1 + k) - 'a']++;
            cnt[s2.charAt(i2 + k) - 'a']--;
        }
        for (int v : cnt) if (v != 0) return false;
        return true;
    }

    // --- optional main for quick testing ---
    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.isScramble("great", "rgeat")); // true
        System.out.println(sol.isScramble("abcde", "caebd")); // false
        System.out.println(sol.isScramble("a", "a"));         // true

        // some trickier cases
        System.out.println(sol.isScramble("abcdefghijklmnopq", "efghijklmnopqcadb")); // false (just example)
    }
}
