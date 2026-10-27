class Solution:
    def reverse(self, x: int) -> int:
        
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1 
        str_num = str(x)
        reverse = 0
        if str_num[0] == "-":
            sign = "-"
            rev_num = str_num[:-len(str_num):-1]
            if sign == "-":
               reverse = sign + rev_num
               # print(reverse)
            else:
               reverse = rev_num
               # print(reverse)
        else:
            reverse = str_num[::-1]
        
        if int(reverse) < MIN_INT or int(reverse) > MAX_INT:
            return 0
        
        return int(reverse)
        
print(Solution().reverse(-123))
        