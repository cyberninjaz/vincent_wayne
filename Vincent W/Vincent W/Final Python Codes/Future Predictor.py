print ("Welcome to the Future Predicticing Operating System or F.P.O.S.") 
computerII = input ("Which subject do you prefer the most? (please enter in lowercase letters) : ") 
if computerII == "mathematics":
    computerIII = input ("What type of math do you prefer? Math mixed with economics, or math mixed with natural science. (please enter in lowercase letters) : ") 
    if computerIII == "economics":
        print ("There's no doubt to it, you will eventually become a financial advisor.") 
    elif computerIII == "natural science":
        a = input ("Would you like to use your knlowledge to build machines or discover new things? (please enter in lowercase letters) : ")
        if a == "build machines": 
            print ("You will become a great engineer.") 
        elif a == "discover new things" :
            print ("You will eventually become a physicist.") 
        else:
             print ("Error. See inventor for immediate help.") 
    else:
        print ("Error. See inventor for immediate help.") 
elif computerII == "science":
    b = input ("Do you like medical science, social science, or natural science (please enter in lowercase letters) : ") 
    if b == "medical science":
        c = input ("Are you good in high pressure situations? (please enter in lowercase letters) : ") 
        if c == "yes":
            print ("You may become either a surgeon or a nuclear medicing anisegiologist.") 
        elif c == "no":
            print ("You will become a standard pediatric doctor in an office.") 
        else:
            print ("Error. See inventor for immediate help.") 
    elif b == "natural science":
        d = input("Do you want to study something involving nature? (please enter in lowercase letters) : ") 
        if d == "yes":
            print ("You will eventually become a biologist.") 
        elif d == "no": 
            print ("You will eventually. become a physicist.") 
        else:
            print ("Error. See inventor for immediate help.") 
    elif b == "social science":
        e = ("Do you want to study something involving education? (please enter in lowercase letters) : ") 
        if e == "yes":
            print ("You will become a educational researcher.") 
        elif e == "no":
            print ("You will become a psycologist.") 
        else:
            print ("Error. See inventor for immediate help.") 
    else:
        print ("Error. See inventor for immediate help.") 
elif computerII == "writing":
    f = input ("Do you like to write a lot or do things relating to writing? (please enter in lowercase letters) : ") 
    if f == "write a lot" :
        print ("You will become an author. Remember, for this job, it is good to have a backup professsion.")
    elif f == "do things relating to writing":
        g = input  ("Do you like law? (please enter in lowercase letters) : ") 
        if g == "yes":
            print ("It is likely you will become a lawyer and maybe eventually become a judge.")
        elif g == "no":
            print ("You woll be a great scribe.")
        else:
            print ("Error. See inventor for immediate help.") 
    else:
        print ("Error. See inventor for immediate help.") 
elif computerII == "buisiness/economics":
    h = input ("Do you like buisiness or economics.") 
    if h == "economics":
        i = input ("Would you prefer education or politics? (please enter in lowercase letters) : ") 
        if i == "education":
            j = input ("Would you like reasearch or would you like to teach? (please enter in lowercase letters) : ") 
            if j == "reasearch":
                print ("You would become an educational reasearcher later in your life.") 
            elif j == "teach":
                print ("You will become a teacher later in your life.") 
            else:
                print ("Error. See inventor for immediate help.") 
        elif i == "politics":
            k = input ("Would you like to work for the legistative branch or the judiciary branch? (please enter in lowercase letters) :  ")
            if k == "legistlative branch":
                l = input ("Do you want to be famous around the world? (please enter in lowercase letters) : ") 
                if l == "no":
                    print ("You will eventually become a member of the U.S. Congress. : ")
                elif l == "yes":
                    print ("In the future, you would become a senator or representative, and maybe even become the president of the United States of America.") 
                else:
                    print ("Error. See inventor for immediate help.")
            elif k == "judiciary branch":
                print ("In the future, you will become a supreme court justice.") 
            else:
                print ("Error. See inventor for immediate help.")
        else:
            print ("Error. See inventor for immediate help.") 
    elif h == "buisiness":
        m = input ("Would you like to start a buisness? (please enter in lowercase letters.) : ")
        if m == "yes":
            n = input ("Would you like to sell other products or design tech? (please enter in lowercase letters) : ")
            if n == "sell other products":
                print ("You will become a buisinessman or woman like Jeff Bezos") 
            elif n == "design tech":
                print ("You will become a buisinessman or woman who will own a large tech company like apple.") 
            else:
                print ("Error. See inventor for immediate help.") 
        else:
            print ("Error. See inventor for immediate help.") 
    else:
        print ("Error. See inventor for immediate help.") 
else:
    print ("Error. See inventor for immediate help.") 