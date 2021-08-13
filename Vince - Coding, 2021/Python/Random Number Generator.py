score = 0
while score == 0:
    a = input ("What is your starting number for generating? : ")
    a = int (a)
    b = input ("What is your ending number for generating? : ")
    b = int (b)
    import random
    print ("Your random number is",random.randint (a, b))
    print (" ")
    print ("Would you like to run the program again?")
    print ("a. Yes")
    print ("b. No")
    c = input ("Please enter your answer here. : ")
    if c == "a":
        print (" ")
    elif c == "b":
        print (" ")
        score = score+1
    else:
        print ("Error")
print ("Okay! Hope this program was helpful for you!")