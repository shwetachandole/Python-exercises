# https://leetcode.com/problems/roman-to-integer

    def romanToInt(self, s: str) -> int:
        rd = {        'I':1,
                      'IV':4,
                      'V':5,
                      'IX':9,
                      'X':10,
                      'XL':40,
                      'L':50,
                      'XC':90,
                      'C':100,
                      'CD':400,
                      'D':500,
                      'CM':900,
                      'M': 1000}
        i = len(s)
        num = 0
        
        while i > 0:
            if s[i-2:i] in rd:
                num += rd[s[i-2:i]]
                i -= 2
            elif s[i-1] in rd:
                num += rd[s[i-1]]
                i -= 1

        return num
