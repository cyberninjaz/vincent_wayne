computerII = input("Please enter a number. ")
computerIII = input("Please enter a number. ") 
computerIV = input("Please enter a number. ") 
computerV = input("Please enter a number. ") 
l= input("Which operation do you want to use? ")
computerII = float (computerII) 
computerIII = float (computerIII) 
computerIV = float (computerIV) 
computerV = float (computerV) 
if l == "+":
    print (computerII + computerIII + computerIV + computerV) 
elif l == "-":
    print (computerII - computerIII - computerIV - computerV)
elif l == "x":
    print (computerII * computerIII * computerIV * computerV)
elif l == "%":
    print (computerII / computerIII / computerIV / computerV)
else:
    print ("Please enter +, -, x, or %. Otherwise see operator for clarification. ") 