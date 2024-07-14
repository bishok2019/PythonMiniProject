class Solution:
    def intToRoman(self, num):
        val = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        roman_numeral =""
        for i,r in val:
            while num >= i:
                roman_numeral  += r
                num -= i
        return roman_numeral

n = int(input("Enter an integers: "))
result = Solution().intToRoman(n)
print(result)