def isPalindrome(self, s):
    s = ''.join(i.lower() for i in s if i.isalnum())
    return s == s[::-1]