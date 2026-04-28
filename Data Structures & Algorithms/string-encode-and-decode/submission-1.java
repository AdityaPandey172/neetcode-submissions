class Solution {

    public String encode(List<String> strs) {
        StringBuilder encoded = new StringBuilder();

        for (String s : strs) {
            encoded.append(s.length()).append("#").append(s);
        }
        return encoded.toString();
    }

    public List<String> decode(String str) {
            List<String> decoded = new ArrayList<>();
            int i = 0;

            while (i < str.length()) {
                int delimiterIndex = str.indexOf('#', i);
                int size = Integer.parseInt(str.substring(i, delimiterIndex));
                int start = delimiterIndex + 1;
                int end = start + size;

                decoded.add(str.substring(start, end));
                i = end;
            }
        return decoded;
    }
        
}

