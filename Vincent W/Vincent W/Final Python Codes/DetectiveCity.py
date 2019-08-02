#DetectiveCity should show a map of the city in the terminal and in each place, list rooms and areas. it should use loops to design the map of the city.
print ("The year is 1954 and the city of Lectorville is in deep destress. Recently the mayor of the city was murdered mysteriously, since then the city is corrupt. The murderer also stole a paper that would show who the next mayor will be. Your name is Dr. Livingstone, and you have to capture the convict and find the paper to determine the next mayor. You are now in your appartment. In the end, you have to present the slip to the courtroom. You have a slip in your notebook saying you should start in the school.")
gameover = False
while gameover == False:
    a = input("Where do you want to go? ")  
    if a == "school":
        b = input ("Do you go in the classroom or the basement? ")
        if  b == "classroom":
            c = input (" When you enter the classroom you notice the teacher dead, lying on the ground. There is blood splattered across the floor. Do you examine the c-orpse, or run away screaming. ")
            if c == "run away screaming":
                print (" Start over and be brave.") 
                continue 
            elif c == "examine the corpse":
                print ("The teacher appears to have a stabbed. You notice footprints that lead to the school library. ")
                d = input ("Do you follow the footprints to the school library, or examine the room again. ") 
                if d == "follow the footprints to the school library":
                    print ("There is a large book open on the library table. There is a slip inside the book saying :  Mayor's mansion key code is 1930 enter through sewer. ") 
                    continue
                elif d == "examine the room again":
                    print ("You find nothing else")
                    print ("Now that you found nothing else in the classroom, you now follow the footprints to the school library. There is a large book open on the library table. There is a slip inside the book saying : mansion key code is 1930 enter through the sewer.")
                    continue
                else:
                    print ("Error. See inventor for immediate help.")
                    continue
            else:
                print ("Error. See inventor for immediate help.") 
                continue
        elif b == "basement":
            print ("When you enter the basement you find dung on the ground.")
            e = input ("Do you examine the dung, or do you continue to walk around the basement.") 
            if e == "examine the dung": 
                print ("As you examine the dung a large dog comes running towards you a eats you alive. Luckily you are immortal, and you can start this game again.") 
                continue
            elif e == "continue to walk around the basement":
                print ("As you walk around the basement a large dog comes running towards you a eats you alive. Luckily you are immortal, and you can start this game again.") 
                continue
            else: 
                print ("Error. See inventor for immediate help.")
        else: 
            print ("Does not compute startover and see inventor")
    elif a == "sewer":
        print("After a long walk you finally arrive a the main sewer. You see many pieces of trash floating down the in the water, and you see a mysterious wooden box.") 
        f = input ("Do you take the wooden box out of the sewer or do you ignore it? ")
        if f == "take the wooden box out of the sewer":
            print ("When you open the box, you find a note scribbled inside it : beware of Alligators. Suddenly an Alligator appears an swallows you whole.") 
            continue
        elif f == "ignore it":
            print (" As you walk in the sewer, you finally reach an intersection. One path leads to the right and the other path leads to the left.") 
            g = input ("Which path fo you chose? ") 
            if g == "left":
                print ("After a few minutes when you enter the left path, you see a swamp full of alligators. You are eaten alive.") 
                continue
            elif g == "right":
                print ("You continue to walk on this path for miles until you find an iron gate.") 
                h = input (" There is a keypad. Enter the code you learned. : ")
                if h == "1930":
                    print ("The gate opens and you walk happily through the passageway. You soon exit out of the sewer and enter the mansion's kitchen. ") 
                    i = input ("The kitchen is deserted exept another body is lyinging on the ground. You take a look at the corpse. He was tricked into drinking lethal poision. You soon come to a crossroad. There are two staircases. Which one do you chose? ") 
                    if i == "staircase 1":
                        print ("You climb up the tall staircase in the mansion. It seems to go on forever. You arrive at the top and see two french doors.")
                        j = input ("Which door do you chose? Door 1 or door 2? ") 
                        if j == "door 1":
                            print ("When you enter thorough the door, a secret chasm opens and you plunge to your death.") 
                            continue
                        elif j == "door 2":
                            print ("You arrive at the master bedroom, the scene of the vicious murder. There is blood splatered across the sheets. You notice the is a slip tucked in the pillow. It says : machine code : 1010   secret code **** to mayor's vault in bank. You decide to take it to your apartment to test it on your investigation machines.") 
                            continue
                        else:
                            print ("Error. See inventor for immediate help and start over.")
                            continue
                    elif i == "staircase 2":
                        print ("You climb up the tall staircase in the mansion. It seems to go on forever. You arrive at the top and see two french doors.")
                        k = input ("Which door do you chose? Door 1 or door 2? ") 
                        if k == "door 1":
                            print ("When you enter thorough the door, a secret chasm opens and you plunge to your death. Start over.") 
                            continue
                        elif k == "door 2":
                            print ("You arrive at the master bedroom, the scene of the vicious murder. There is blood splatered across the sheets. You notice the is a slip tucked in the pillow. It says : machine code : 1010   secret code **** to mayor's vault in bank. You decide to take it to your apartment to test it on your investigation machines.") 
                            continue
                        else:
                            print ("Error. See inventor for immediate help and start over.")
                            continue
                    else:
                        print ("Error. See inventor for immediate help and start over.")
                        continue 
                else:
                        print (" Just as you entered your code, a giant anvil appears out of the ceiling and falls on your head. You die. Start over.") 
                        continue            
            else:
                print ("Error. See inventor for immediate help and start over.")
                continue
        else:
            print ("Error. See inventor for immediate help and start over.")
    elif a == "apartment":
        print ("You are now in your apartment. You inserted the slip in the mansion in your detective machine.") 
        m = input ("Please enter the machine code to uncover the slip : ") 
        if m == "1010":
            print ("The machine scans through the message and prints the secret message : secret code is 1456 to mayor's vault in the bank. You now decide to travel to the bank.")
            continue
        else:
            print ("Because you entered the wrong code, your detective machine explodes and kills you.") 
            continue
    elif a == "bank":
        n = input ("After a short walk you finally arrive at the bank. You meet a clerk at the bank. Do you ask him to take you to the vault or do you bribe him to do it with $100 ")
        if n == "bribe him":
            print ("The worker exepts the money and takes you down to the vault. On the way there, he says to go in a closet. Do you listen to him, or run the way he was leading you to?")
            o = input ("Do you want to run or listen to what he says? ")
            if o == "run":
                print ("You quickly sprint away from the man as he shouts for the police. You find and air vent on the wall and you climb through it. You soon enter a crossroad.") 
                p = input ("Which path do you chose? The the right air vent, or the left air vent. ")
                if p == "right":
                    print ("After a long walk in the vent, the vent opens into a trash incinerator. You die. Start over.") 
                    continue
                elif p == "left":
                    print ("After a long walk in the air vent you soon enter the front of the vault. You see a keypad.") 
                    q = input ("Enter the code to open the vault. : ") 
                    if q == "1456":
                        print ("The vault opens. You find mounds of gold coins and bags of money, but that doesen't matter to you. There is a note printed on one of the gold coins. It says, (Dear Detective: There is a man who is about to murder me. I do not know his wherabouts, but I know on July 18th he will meet in the park with his friends and try to take over Lectorville. Park key code is 8768. Sincerely, Mayor Lector.) ") 
                        continue  
                    else:
                        ("As you entered the code, a giant anvil knocks you in the head and kills you. You die. Start over.")
                        continue 
                else:
                    print ("Error. See inventor for immediate help and start over.")
                    continue
            elif o == "listen to him":
                print ("Once you are inside the closet he locks you in and finds the police. They knock you unconcious and you die. Start over.")
                continue
            else:
                print ("Error. See inventor for immediate help and start over.")
                continue
        elif n == "ask him":
            print ("The worker quickly signals the police at the bank. They knock you unconcious and you die. Start over")
            continue
        else:
            print ("Error. See inventor for immediate help and start over.")
            continue 
    elif a == "park":
        print ("After a short drive, you finally reach the gates of the park. It is nighttime and the gates are securely closed. You notice a keypad next to one of the gates.")
        aa = input ("Enter the key code to open the gate. : ")
        if aa == "8768":
            print ("The door makes a whirring sound, and clicks open. Not long after you enter, you come to a crossroad.")
            bb = input ("One path leads to the left, while the other leads to the right. Which one do you chose? ") 
            if bb == "left":
                print ("While you are walking through the path you see a note on the ground.") 
                cc = input ("Do you attempt to look at the note, or do you want to ignore it? ") 
                if cc == "look at the note":
                    print ("You bend down to read the note, and it says : BEWARE OF FALLING TREES. Then, a tree russels and falls on top of you. You die. Start over.")
                    continue
                elif cc == "ignore it":
                    print ("As you continue down the path, a giant tree topples on you. You die. Start over.")
                    continue
                else:
                    print ("Error. See inventor for immediate help and start over.") 
                    continue
            elif bb == "right":
                print ("Not after a while, you come to another set of crossroads. One of them leads to right and goes into a dense forest, while the other leads to the left and goes into the gardens.")
                dd = input ("Which path do you chose? ") 
                if dd == "left":
                    print ("After you walk on the path for a few minutes, you encounter a large man. He punches you and you pass out. You die. Start over.")
                    continue
                elif dd == "right":
                    print ("After you walk on the path for a few minutes, you find a faint glow in a tree. You realize it is the villan's secret hideout. As you start to climb a ladder, two villans pop out and attack you.") 
                    ee = input ("The villans chase you all the way to the gardens. You see a large fountain. Do you want to jump into it, or keep on running.")
                    if ee == "keep on running":
                        print (" The robbers soon gain on you an knock you out. You die. Start over.") 
                        continue
                    elif ee == "jump into it":
                        print ("You jump into it, and the robbers pass you, not knowing you are even there. In the fountain you see a slip. It says : Mayor - The murderer his attempting to kill me is going to attend a party in the trade center to take over the city. Enter through the top of the building. You will need to parachute. The roof door code is potatoes.") 
                        continue
                    else:
                        print ("Error. See inventor for immediate help and start over.") 
                        continue
                else:
                    print ("Error. See inventor for immediate help and start over.") 
                    continue
            else:
                print ("Error. See inventor for immediate help and start over.") 
                continue 
        else: 
            print ("Just as you entered the code, an alarm sounded the police came running out of the nowhere and hit you in the head. You die. Start over.") 
            continue
    elif a == "trade center":
        r = input ("The day comes and you parachute from your helicopter. You arrive at the door. Enter the code : ")
        if r == "potatoes":
            s = input ("You walk across the hallway and it spilts into two. Which one do you pick? The left or the right? ")
            if s == "left":
                t = input ("You walk down the hall and find a man. Do you talk to him or don't talk to him? ")
                if t == "talk to him":
                    u = input ("The man tells you to not continue in the hall but to go in the vent you do so and after a lot of crawling the vent splits into two which way do you go? Left or right? ")
                    if u == "left":
                        print("You continue crawling but you see and alligator in the vent. It swallows you whole and you die. Start over.")
                        continue
                    elif u == "right":
                        print ("You continue down the thin vent and you pop out. You find the mayor's son in a cell crying.")
                        v = input ("Do you free him or do you let him stay incarcerated? ")
                        if v == "free him":
                            print ("When you free him, he tells you to take the elevator to the trade center floor. He says the murderer would be attending a party there.") 
                            w = input ("You enter the elevator and go down to the trade center party. When the doors open, you see the murder dressed up in a suit. Do you tackle him, or do you leave him alone? ") 
                            if w == "tackle him":
                                print ("You know tackle the murderer and rap him in a tight rope. You notice he has a tiny slip inside his pocket. You believe it's the slip that will determine the next mayor. All you have to do now, is to deliver him to the courtroom. A guest tells you the courtroom key code is 2019.") 
                                continue
                            elif w == "leave him alone":
                                print ("As you calmy walk pass the murderer the police come in through the doors. You care caught,and you would go in prision for the rest of your life.") 
                                continue
                            else:
                                print ("Error. See inventor for immediate help and start over.") 
                        elif v == "let him stay incarcerated":
                            print (" a camera spots you a sets of the alarm. The soldiers come in and kill you. Start over.")
                        else:
                            print ("Error. See inventor for immediate help and start over.") 
                            continue
                    else:
                        print ("Error. See inventor for immediate help and start over.")
                        continue
                elif t == "don't talk to him":
                    print ("You walk down the hall and run into a soldier. He kills you so you die. Startover.")
                    continue
                else:
                    print ("Error. See inventor for immediate help and start over.")
                    continue
            elif s == "right":
                print ("You arrive at a bunch of body guards. They knock you unconcious and you die. Startover. ")
            else:
                print ("Error. See inventor for immediate help and start over.")
                continue
        else:
            print ("Just after you typed the code in the ground under you opens up and you fall and die. Start over")
            continue
    elif a == "courtroom":
        print ("You arrive at the entrance of the courtroom. There is a keypad for you to enter the code in.")
        x = input ("Enter the key code : ")
        if x == "2019":
            print ("When you finally got in the courtroom, you presented the murderer and the slip. The judges discovered that the murderer was actually the mayor's twin brother. The judges also discovered that the slip proclaimed you as the next mayor. Hooray you won the game! ") 
            break 
        else:
            print ("Just as you entered the keycode gap opens beneath the entrance and swallows you up. You die. Start over. ")
    else:
        print ("Does not compute startover and see inventor")
        continue