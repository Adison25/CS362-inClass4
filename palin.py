def palindrome():
    check = 0
    str = input("Please enter a string: ") 
    #check input
    for i in range(len(str)):
        if str[i] == str[len(str)-i-1]:
            check = check + 1
    if check == len(str):
        return 1
    return 0
