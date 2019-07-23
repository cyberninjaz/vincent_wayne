computerII = input("Please enter a number. ") 
computerIII = input("Please enter a number. ") 
computerIV = input ("Which operation do you want to use? ") 
computerII = float (computerII) 
computerIII = float (computerIII)
if computerIV == "+":
    print (computerII + computerIII) 
elif computerIV == "-":
    print (computerII + computerIII)
elif computerIV == "x":
    print (computerII * computerIII)
elif computerIV == "%":
    print (computerII/computerIII)
else:
    print ("Please enter +, -, x, or %. Otherwise see operator for clarification. ") 