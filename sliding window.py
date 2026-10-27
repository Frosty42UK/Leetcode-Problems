'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
       if len(s) < 2:    # empty string or string length < 2
          return len(s)
          
       final_length = 0
       l1 = [s[0]]
       
       for i in range(1, len(s)):
           if s[i] not in l1:
               l1.append(s[i])
               # print(len(l1))
           else:
               index = l1.index(s[i])
               l1 = l1[index + 1 :]
               l1.append(s[i])
               
           if final_length < len(l1):
               final_length = len(l1)
           
       return final_length
                  
solution = Solution()
answer = solution.lengthOfLongestSubstring("")

print(answer)
