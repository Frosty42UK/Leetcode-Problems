'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
       if numRows < 1:
           return ""
        
       if numRows == 1: # edge case handled
           return s
          
       rows = 1   
       direction = 1
       matrix = [[] for _ in range(numRows)] # _ -> indicates only repeating the loop
       indexM = 0
       
       for i in range(len(s)):
           if direction == 1:
               matrix[indexM].append(s[i])
               indexM += 1
               rows+=1
               if rows == numRows:
                   direction = -1
           else:
               matrix[indexM].append(s[i])
               indexM -= 1
               rows -= 1
               if rows == 1:
                   direction = 1
           
       return "".join(["".join(row) for row in matrix])
           
           
        
print(Solution().convert("PAYPALISHIRING", 0))        
        