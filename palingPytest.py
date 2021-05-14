def palindrome(str):
   check = 0
   #check input
   for i in range(len(str)):
      if str[i] == str[len(str)-i-1]:
         check = check + 1
   if check == len(str):
      return True
   return False

def test_palindromeTrue():
   assert palindrome("maam")
   assert palindrome("1221")
   assert palindrome("124421")

def test_palindromeFalse():
   assert not palindrome("mamm")
   assert not palindrome("sack")
   assert not palindrome("1231")