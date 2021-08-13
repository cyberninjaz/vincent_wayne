score = 0
while score == 0:
    ta = input ("Please enter your first number. : ")
    a = float (ta)
    tb = input ("Please enter your second number. : ")
    b = float (tb)
    print ("Please select which operation you would like to use.")
    print ("a. Addition")
    print ("b. Subtraction")
    print ("c. Multiplication")
    print ("d. Division")
    c = input ("Which operation would you like? : ")
    if c == "a":
        t = a+b
    elif c == "b":
        t = a-b
    elif c == "c":
        t = a*b
    elif c == "d":
        t = a/b
    print (" ")
    print ("Your answer is ", t)
    print (" ")
    print ("Would you like to run the program again?")
    print ("a. Yes")
    print ("b. No")
    d = input ("Please enter your answer here. : ")
    if d == "a":
        print (" ")
    elif d == "b":
        print (" ")
        score = score + 1
    else:
        print ("Error")
print ("Okay! Hope this promgram was helpful for you!")