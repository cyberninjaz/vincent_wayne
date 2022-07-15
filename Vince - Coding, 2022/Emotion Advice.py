
run = 0
while run == 0:
    print (" ")
    print ("Are you:")
    print("a. Tired")
    print("b. Hangry")
    print("c. Energetic")
    print("d. Stressed")
    print("e. Crazy")
    ComputerII = input("Type in the letter: ")
    print(" ")
    if ComputerII == "a" or ComputerII == "A":
        print ("Take a nap.")
    elif ComputerII == "b" or ComputerII == "B":
        print ("Eat something.")
    elif ComputerII == "c" or ComputerII == "C":
        print ("Go exercize.")
    elif ComputerII == "d" or ComputerII == "D":
        print ("Go take a break.")
    elif ComputerII == "e" or ComputerII == "E":
        print ("Calm Down.")
    else:
        print ("Ya didn't follow the instructions.")
    
    print (" ")
    print ("Do you want to do the program again?")
    a = input ("Type yes or no in all lowercase: ")
    if a == "yes":
        run == 0
    elif a == "no":
        run = run+1
    else:
        print (" ")
        print ("Ya didn't follow the instructions.")