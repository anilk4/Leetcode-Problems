class Solution {
    public boolean isPalindrome(int x) {
        String s = String.valueOf(x); // Convert int to String
        String reversed = new StringBuilder(s).reverse().toString(); // Reverse the string
        return s.equals(reversed); // Compare original and reversed strings
    }
}
