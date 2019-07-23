while True:
    computerII = input (" Rock, Paper, Scissors, Shoot! ( please enter in lowercase letters)(If you want to quit, write i quit.): ") 
    if computerII == ("paper"): 
        print ("The computer plays scissors. You lose.") 
    elif computerII == ("scissors"): 
        print ("The computer plays rock. You lose.") 
    elif computerII == ("rock"):
        print ("The computer plays paper. You lose.") 
    elif computerII == ("i quit") :
        print ("Okay, have a nice day.") 
        break 
    else:
        print ("You cheated, you lose.") 