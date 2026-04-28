class Solution:
    def isPalindrome(self, x: int) -> bool:
        X = str(x)
        X_reverse = X[::-1]
        if X != X_reverse:
            return False

        return True

