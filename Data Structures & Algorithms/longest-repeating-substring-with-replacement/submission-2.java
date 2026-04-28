class Solution {
    public int characterReplacement(String s, int k) {
        
        int [] occur = new int[26];
        int left = 0;
        int ans = 0;
        int maxOccur = 0;

        for(int right = 0; right < s.length(); right++){
            maxOccur = Math.max(maxOccur, ++occur[s.charAt(right) - 'A']);
            if(right - left + 1 - maxOccur > k){

                occur[s.charAt(left) - 'A']--;
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
