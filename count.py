def count():
    check = 1
    count = input("Please enter a string: ") 
    #check input
    for i in range(len(count)):
        if (i+1 < len(count)) and count[i] != " " and count[i+1] == " ":
            check = check + 1
    return check