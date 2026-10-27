'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        
       if len(s) < 2: # an empty string or a single character is a palindrome
           return s
           
       length = 0
       final_length = 0
       best_start = 0
        
       for i in range(len(s)):
           indexS = i
           indexF = i
           while indexS >= 0 and indexF < len(s) and s[indexS] == s[indexF]:
               indexS -= 1
               indexF += 1
               
           length = indexF - indexS - 1
           if final_length < length:
               final_length = length
               best_start = indexS + 1

       for i in range(len(s)):
           indexS = i
           indexF = i+1
           while indexS >= 0 and indexF < len(s) and s[indexS] == s[indexF]:
               indexS -= 1
               indexF += 1
               
           length = indexF - indexS - 1
           if final_length < length:
               final_length = length
               best_start = indexS + 1       
               
       return s[best_start: final_length + best_start]
                        
    
answer = Solution().longestPalindrome("babad")
print(answer)
