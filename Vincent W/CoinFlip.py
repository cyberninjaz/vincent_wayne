import random 
computerII = input ("To flip the computerized coin type in this word ( Flip! ) : ") 
if computerII == "Flip!":
    computerIII = random.randint (1,2) 
    if computerIII == 1:
        print ("Heads") 
    elif computerIII == 2:
        print ("Tails") 
    else:
        print ("Error") 