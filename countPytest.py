def count(count):
    check = 1
    #check input
    for i in range(len(count)):
        if (i+1 < len(count)) and count[i] != " " and count[i+1] == " ":
            check = check + 1
    return check

def test_palindromeTrue():
   assert count("maam") == 1
   assert count("hi everyone") == 2
   assert count("what up bud") == 3

def test_palindromeFalse():
   assert not count("man what up") == 2
   assert not count("sa ck") == 3
   assert not count("12 3 1") == 4