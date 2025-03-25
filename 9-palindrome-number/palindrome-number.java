class Solution {
    public boolean isPalindrome(int x) {
    int temp=x;
    int n = 0;

    while(x > 0){
        n = n * 10 + (x%10);
        x /= 10;
    }

    return temp == n;
    }
}
