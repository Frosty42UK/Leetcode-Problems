class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        result = 0          
        sign = ""
        has_digits = False  
        is_special = False
        
        if s == "" or s.isalpha():
            return 0
        
        for i in range(len(s)):
            if s[i].isdigit():
                has_digits = True
                
                digit = ord(s[i]) - ord('0')
                result = (result * 10) + digit
                
                if i+1 < len(s) and not(s[i+1].isalpha() or s[i+1].isdigit()):
                    break
                    
            elif s[i] == "-" or s[i] == "+":
                if sign != "":  
                    break
                sign = s[i]
                
            elif s[i].isalpha():
                break
                
            elif not(s[i].isalpha() or s[i].isdigit()):
                is_special = True
                break

        if not has_digits:
            return 0        
                
        if sign == "-":
            result = -result
        
        if is_special:
            return 0
            
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if result < INT_MIN: return INT_MIN
        if result > INT_MAX: return INT_MAX
            
        return result
