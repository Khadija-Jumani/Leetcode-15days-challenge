class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLen = 0;

        // Stores the last seen index of each character
        HashMap<Character, Integer> map = new HashMap<>();

        for (int right = 0; right < s.length(); right++) {
            char ch = s.charAt(right);

            // If the character was seen and is inside the current window
            if (map.containsKey(ch) && map.get(ch) >= left) {
                // Move the left pointer to avoid duplicates
                left = map.get(ch) + 1;
            }

            // Update last seen index
            map.put(ch, right);

            // Calculate current window length
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}
