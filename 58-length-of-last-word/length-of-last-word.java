class Solution {
    public int lengthOfLastWord(String s) {
        if (s == null || s.isEmpty()) return 0;

        s = s.trim(); // remove leading/trailing spaces
        int lastSpace = s.lastIndexOf(' ');
        return s.length() - lastSpace - 1;
    }
}
