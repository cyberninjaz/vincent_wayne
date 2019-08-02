computerIII = 0 
while computerIII<10: 
    if computerIII == 5:
        print ("Keep on going.")
    computerII = input("Hit buttons until number reaches 10. Adding represents + and subtracting represents -. ") 
    if computerII == "+":
        computerIII = computerIII + 1 
        print (computerIII)
    elif computerII == "-":
        computerIII = computerIII - 1
        print (computerIII) 
    else:
        print ("Error. ") 