ComputerII = 0
while ComputerII == 0:
    score = 0
    b = str ()
    a = input ("Please type in your word. : ")
    while score < len (a):
        (a[-1-score])
        b = b + (a[-1-score])
        score = score+1
    if a == b:
        print ("This word is a palindrome.")
    else:
        print ("This word is not a palindrome.")
    print (" ")
    print ("Would you like to run the program again?")
    print ("a. Yes")
    print ("b. No")
    c = input ("Please enter your answer here. : ")
    if c == "a":
        print (" ")
    elif c == "b":
        print (" ")
        ComputerII = ComputerII + 1
    else:
        print ("Error")
print ("Okay! Hope this program was helpful for you!")