"""
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        """
        Approach
            Suppose str1 = "ABCABC" and str2 = "ABC"
            str1 + str2 = ABCABCABC
            str2 + str1 = ABCABCABC
            str1 + str2 == str2 + str1
            return str.substr(0, gcd(size(str1), gcd(size(str2))))
            where gcd(3, 6) = 3
            So, answer is "ABC"

            Also str1 = "LEET", str2 = "CODE"
            str1 + str2 = "LEETCODE"
            str2 + str1 = "CODELEET"
            So, return ""
        """
        # Check if concatenated strings are equal or not, if not return ""
        if str1 + str2 != str2 + str1:
            return ""
        
        # If strings are equal than return the substring from 0 to gcd of len(str1), len(str2)
        from math import gcd 
        # gcd is greatest common divisor
        # Example: gcd(6,4) returns 2, because 2 is the highest divisor for 6 and 4.
        return str1[:gcd(len(str1), len(str2))]
        

print(Solution().gcdOfStrings("ABCABCABC", "ABCABC"))