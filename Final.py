# Brad Rogers
import random
import time

Inventory = [0, 0, 0, 0]
random = random.randint

def main():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Hello, and welcome to my game. This game is styled as a classic")
    print("adventure game and will have you exploring a house.")
    print("")
    print("")
    print("-----------------------------------------------------------")
    print("------------------------Main Menu--------------------------")
    print("")
    print("Type 1 to Start")
    print("")
    print("")
    menu()

def menu():
    menu = int(input(""))
    if menu == 1:
        print(intro())
    else:
        print("Input 1 or 2")
        menu()


def intro():
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("This first think you notice around you is the sound of the clock ticking,")
    print("As your eyes adjust to the darkness, you see that you are in the foyer of ")
    print("a large house. Behind you is a door which appears to lead outside. There is")
    print("a lock on the door and a note on the door that that says 'If you wish to leave")
    print("then you must locate the key to this door.")
    time.sleep(8)
    print(entrance())


def entrance():
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("To your left you see a doorway leading into the living room. In front of you")
    print("there are stairs going upstairs, and beside the stairs you see a hallway. ")
    print("To the right you see a doorway that opens into a dining room.")
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("1. Enter living room")
    print("2. Go upstairs")
    print("3. Go down the hallway")
    print("4. Go into the dining room")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        livingroom()
    elif menu == 2:
        stairs()
    elif menu == 3:
        hall()
    elif menu == 4:
        dining()
    else:
        entrance()


def livingroom():
    print("")
    print("")
    print("---------------------------------------------------------------------------")
    print("Inside the living room you can see that everything is covered in a film of dust, all of ")
    print("the furniture has been covered in plastic sheets. Looking around you notice a fireplace")
    print("with an old painting of a burning house over it.")
    print("")
    print("")
    print("-------------------------------------------------------------------------------")
    print("1. Inspect the room")
    print("2. Inspect the portrait")
    print("3. Inspect the fireplace")
    print("4. Go back to foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("Aside from the picture and the fireplace, nothing stands out.")
        print("------------------------------------------------------------------------------------")
        livingroom()
    elif menu == 2:
        print("There is a picture of an old house sitting in an empty field.")
        livingroom()

    elif menu == 3:
        if Inventory[1] == 0:
            if Inventory[0] == 1:
                print("There are some old looking logs sitting in the hearth. Reaching into your pocket")
                print("you use the lighter to light the fireplace. As the fire lights up the room you ")
                print("notice a key sitting on the mantle. You take the key")
                Inventory[1] = 1
                time.sleep(5)
                livingroom()
            else:
                print("There are some old logs in the fireplace, you have no way to light them")
                livingroom()
        else:
            print("The fireplace has been lit and is radiating heat.")
            livingroom()
    elif menu == 4:
        entrance()

    else:
        livingroom()


def stairs():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Looking upstairs you see a landing where moonlight filters through an old dirty window.")
    print("continuing upwards you hear the stairs creak under you feet, and your footsteps cause dust to")
    print("swirl around in the moonlight. ")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Keep climbing ")
    print("2. Go back down")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        upstairs()
    elif menu == 2:
        entrance()
    else:
        print("Input 1 or 2")
        stairs()

def upstairs():
    if Inventory [2] == 1:
        if Inventory[3] == 1:
            print("Putting both keys together you decide to leave the house, going down the stairs quickly. As you")
            print("approach the front door you see the lock by the handle. Using the key you open the door and head")
            print("outside. Once you get far enough away you turn around and see the house standing behind you.")
            houseOutside()

    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("The upstairs opens to a landing, and there are five doorways. Two on the left, two on the right,")
    print("and one across from the stairs. Which one do you try?")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. First door on left")
    print("2. Second door on left")
    print("3. Door in the middle")
    print("4. First door on right")
    print("5. Second door on right")
    print("6. Go back downstairs")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        if Inventory[2] == 1:
            print("I have already explored the library, there is nothing else I need there.")
            time.sleep(4)
            upstairs()
        else:
            if Inventory[1] == 1:
                print("The door appears to be locked, you can make out a keyhole. Trying the key that you found")
                print("reveals that it fits the lock, the door slowly swings open. ")
                time.sleep(5)
                library()
            else:
                print("The door appears to be locked, you can make out a keyhole. You do not have a key for it.")
                time.sleep(5)
                upstairs()
    elif menu == 2:
        print("Trying the door, the knob turns and you walk inside.")
        time.sleep(4)
        firstBedroom()
    elif menu == 3:
        print("Trying the door, the knob turns and you walk inside.")
        time.sleep(4)
        bathroom()
    elif menu == 4:
        print("Trying the door, the knob turns and you walk inside.")
        time.sleep(4)
        secondBedroom()
    elif menu == 5:
        print("Trying the door, the knob turns and you walk inside.")
        time.sleep(4)
        thirdBedroom()
    elif menu == 6:
        print("Going back downstairs you reach the foyer.")
        time.sleep(4)
        entrance()
    else:
        upstairs()

def library():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Entering the room you see that it everything is covered in a thick layer of dust. On  ")
    print("the walls are rows upon rows of books. Punctuating the shelves are windows allowing")
    print("in light from the outside. in the center of the room is a table with two chairs.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Inspect the table")
    print("2. Inspect the shelves")
    print("3. Leave the room")
    print("")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("Walking up to the table you see it is an old chessboard, the pieces look like they")
        print("are set up to play a game.")
        time.sleep(5)
        library()
    elif menu == 2:
        print("")
        print("")
        print("Inspecting the shelves it seems like most of the books are very old and contain")
        print("unfamiliar names. Like the rest of the room they seem like they have remained")
        print("undisturbed for years.")
        time.sleep(5)
        print("")
        print("")
        print("------------------------------------------------------------------------------------")
        print("1. Inspect the table")
        print("2. Inspect the shelves")
        print("3. Leave the room")
        print("")
        print("")
        print("")
        menu = int(input(""))
        if menu == 1:
            print("")
            print("")
            print("Walking up to the table you see it is an old chessboard, the pieces look like they")
            print("are set up to play a game.")
            time.sleep(5)
            library()
        elif menu == 2:
            print("")
            print("")
            print("Continuing your inspection of the shelves you find a book that looks more worn than the")
            print("other books you have seen. The title has been worn off.")
            print("")
            print("")
            print("------------------------------------------------------------------------------------")
            print("1. Inspect the table")
            print("2. Remove the book")
            print("3. Leave the room")
            print("")
            print("")
            menu = int(input(""))
            if menu == 1:
                print("")
                print("")
                print("Walking up to the table you see it is an old chessboard, the pieces look like they")
                print("are set up to play a game.")
                time.sleep(5)
                library()
            elif menu == 2:
                print("")
                print("")
                print("As you begin to pull the book off of the shelf you hear a click and see the shelf start to")
                print("swing open. Behind the shelf there is what appears to be a hidden room.")
                print("")
                print("")
                time.sleep(5)
                print("Overcome by curiosity you enter the room to find out what was so important to be hidden")
                print("behind a locked door and a false wall.")
                print("------------------------------------------------------------------------------------")
                time.sleep(5)
                hiddenRoom()

            elif menu == 3:
                print("Leaving the room you return to the staircase.")
                upstairs()
            else:
                library()
        elif menu == 3:
            print("Leaving the room you return to the staircase.")
            upstairs()
        else:
            library()
    elif menu == 3:
        print("Leaving the room you return to the staircase.")
        upstairs()
    else:
        library()

def hiddenRoom():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("The room appears to be cloaked in darkness and you are unable to make anything out. Pulling out the")
    print("lighter you illuminate the darkness. In the center of the room is something covered under a large")
    print("white sheet.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Pull back the sheet")
    print("2. Inspect the room")
    print("3. Leave the room")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("Removing the sheet you see a collection of antique furniture hidden under a blanket. On top of the ")
        print("furniture you see a note and half of a key")
        print("")
        print("")
        print("------------------------------------------------------------------------------------")
        print("1. Read the note")
        print("")
        print("")
        menu = int(input(""))
        if menu == 1:
            print("")
            print("")
            print("The note is written in script, it reads 'Thank you for coming to my house, the half of the")
            print("key that is with this note is part of what you need in order to escape. I hope you enjoy your")
            print("stay.")
            time.sleep(5)
            Inventory[2] = 1
            print("Taking the key you leave the room. As you walk past the bookcase you hear a click as you step")
            print("on the floor, the bookcase swings back shutting the passage behind you. ")
            time.sleep(5)
            upstairs()
        else:
            hiddenRoom()
    elif menu == 2:
        print("The room appears to be empty except for the pile in the center")
        time.sleep(5)
        hiddenRoom()
    else:
        print("Input 1 or 2")


def firstBedroom():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Entering the room you see what appears to be a bedroom. Taking a step forward causes the board")
    print("underneath your foot to break, it appears that this room has become unstable and is not safe to")
    print("enter.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Continue in")
    print("2. Return to the foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("The floor breaks beneath your feet and everything goes black.")
        print("")
        print("")
        print("------------------------------------Game Over-----------------------------------------")
        print("")
        print("")
        time.sleep(5)
        Inventory[0] = 0
        Inventory[1] = 0
        Inventory[2] = 0
        Inventory[3] = 0
        main()
    elif menu == 2:
        print("Deciding its unsafe you return to the staircase")
        time.sleep(5)
        upstairs()
    else:
        firstBedroom()

def bathroom():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Walking into the bathroom it appears to be an old bathroom. Tiles are missing from the")
    print("walls and the floor. The room appears to hold nothing of value.")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Inspect the bathroom")
    print("2. Return to the foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("The bathroom is in a state of disrepair, nothing about it stands out however")
        print("")
        time.sleep(4)
        bathroom()
    elif menu == 2:
        print("Leaving the bathroom you return to the previous room.")
        time.sleep(4)
        upstairs()
    else:
        bathroom()


def secondBedroom():
    if Inventory[3] == 0:
        print("")
        print("")
        print("------------------------------------------------------------------------------------")
        print("This room appears to be a bedroom, there is a large bed in the center of the room, and on each side")
        print("of the bed there is a door")
        print("")
        print("")
        print("------------------------------------------------------------------------------------")
        print("1. Inspect the bed")
        print("2. Inspect the first door")
        print("3. Inspect the second door")
        print("4. Leave the room")
        print("")
        print("")
        menu = int(input(""))
        if menu == 1:
            print("The bed appears to be made, upon inspecting it closer there was a envelops shoved under the")
            print("pillow. Opening the envelope reveals part of a key. Looking around the room revealing nothing else")
            print("of value, you return to the other room.")
            print("")
            Inventory[3] = 1
            upstairs()

        elif menu == 2:
            print("Opening the door reveals a closet filled with old clothes. After looking through the closet you")
            print("do not find anything of value")
            time.sleep(5)
            secondBedroom()
        elif menu == 3:
            print("Opening the door on the far side of the bed reveals a closet filled with boxes. They appear to")
            print("contain old newspapers.")
            time.sleep(5)
            secondBedroom()
        elif menu == 4:
            print("Leaving the room you return to the upstairs stairway.")
            time.sleep(5)
        else:
            bathroom()
    else:
        print("I have already explored that room, no need to go back in there.")
        time.sleep(5)
        upstairs()

def thirdBedroom():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Opening the door reveals a child's bedroom, there are old toys strewn about the floor and the bed")
    print("appears to be too small for an adult. ")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Inspect the room")
    print("2. Return to the foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("The room appears to be normal.")
        time.sleep(5)
        thirdBedroom()
    elif menu == 2:
        print("Leaving you return to the previous room.")
        time.sleep(5)
        upstairs()
    else:
        thirdBedroom()


def dining():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("The dining room is taken up by a huge table, and you can vaguely see that it has ")
    print("had places set at teh table, the cobwebs covering everything indicate that it was ")
    print("done a long time ago.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Inspect the table")
    print("2. Return to the foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("There are a bunch of antique plates and utensils set in a orderly fashion ")
        time.sleep(5)
        dining()
    elif menu == 2:
        entrance()
    else:
        print("Input 1 or 2")
        print(dining())

def hall():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Walking down the hallway you see a door on the right, leading into a kitchen. Further")
    print("down the hall you see what looks like a old grandfather clock ticking in a room at the ")
    print("rear of the house.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Enter the kitchen")
    print("2. Go further down the hall")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        kitchen()
    elif menu == 2:
        porch()
    else:
        hall()

def kitchen():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Entering the kitchen you see it appears to be filled with old appliances. There are two")
    print("windows on the wall which allow in the moonlight. Against the other wall you see a wall")
    print("of cabinets, and beneath that an old stove. There appears to be a door leading to a large")
    print("room, and the entrance to the hallway.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Investigate the cabinets")
    print("2. Go to hallway")
    print("3. Enter the room")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("Opening the cabinets you see that they are filled with old cooking and dining utensils.")
        print("There does not appear to be anything of value.")
        time.sleep(5)
        kitchen()
    elif menu == 2:
        hallA()
    elif menu == 3:
        sunroom()
    else:
        print(entrance())

def hallA():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Reaching the hallway, which path do you take? ")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Enter the kitchen")
    print("2. Go further down the hall")
    print("3. Head to foyer")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        kitchen()
    elif menu == 2:
        porch()
    elif menu == 3:
        entrance()
    else:
        hallA()

def porch():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("Reaching the end of the hall and entering the room you see an old clock, and two open")
    print("doorways on either side. This part of the house appears to be in a state of disrepair,")
    print("and the wood on the walls and the floors appear to be rotten.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Investigate the doorway on the left")
    print("2. Investigate the doorway on the right")
    print("3. Examine the clock")
    print("4. Return to the hallway")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("From the entrance you can see that this room used to be a laundry room, but the floor")
        print("appears to have collapsed.")
        porchA()
    elif menu == 2:
        print("This appears to be an old bathroom, the floor has collapsed and everything appears to")
        print("be rotten. ")
        porchA()
    elif menu == 3:
        print("Approaching the clock you hear it ticking, Upon closer inspection however the hands on")
        print("the clock are not moving. The hands appear to be stuck at 7:27")
        time.sleep(5)
        porchA()
    elif menu == 4:
        hallA()
    else:
        porchA()

def porchA():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("In front of you stands the clock, and on either side of the clock stands a doorway. Behind")
    print("you is the hallway. What do you do next?")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Investigate the doorway on the left")
    print("2. Investigate the doorway on the right")
    print("3. Examine the clock")
    print("4. Return to the hallway")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        print("From the entrance you can see that this room used to be a laundry room, but the floor")
        print("appears to have collapsed.")
        porchA()
    elif menu == 2:
        print("This appears to be an old bathroom, the floor has collapsed and everything appears to")
        print("be rotten. ")
        porchA()
    elif menu == 3:
        print("Approaching the clock you hear it ticking, Upon closer inspection however the hands on")
        print("the clock are not moving. The hands appear to be stuck at 7:27.")
        time.sleep(5)
        porchA()
    elif menu == 4:

        hallA()
    else:
        porchA()

def sunroom():
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("This room seems to be huge, but strangely empty. Windows line three of the walls, and")
    print("they serve to illuminate a safe, which appears to be the sole thing of interest in the room.")
    print("")
    print("")
    print("------------------------------------------------------------------------------------")
    print("1. Inspect the safe")
    print("2. Return to the hallway")
    print("")
    print("")
    menu = int(input(""))
    if menu == 1:
        if Inventory[0] == 1:
            print(" You already opened the safe and have the key")
            sunroom()
        else:
            print("The safe appears to have a combination lock, would you like to input a password")
            print("1. for yes")
            print("2. for no")
            print("")
            print("")
            menu = int(input(""))
            if menu == 1:
                print("input first digit")
                first = int(input(""))
                print("Input second digit")
                second = int(input(""))
                print("Input third digit")
                third = int(input(""))
                if first == 7:
                    if second == 2:
                        if third == 7:
                            print("The safe swings open and reveals a lighter, picking it up you put it in your pocket.")
                            Inventory[0] = 1
                            time.sleep(3)
                            sunroom()
                        else:
                            print("The password did not work.")
                            time.sleep(3)
                            sunroom()
                    else:
                        print("The password did not work.")
                        time.sleep(3)
                        sunroom()
                else:
                    print("The password did not work.")
                    time.sleep(3)
                    sunroom()
            else:
                sunroom()
    elif menu == 2:
        sunroom()
    else:
        sunroom()

def houseOutside():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("77$7$$77O$8ZZ$ZDDONNNMM8ZZ78OD7ZO8MMMMNO$ONDNNNMMMMMM8N8OD7NDMMMM8D$88$O777777777777777777?~$77777777777777777777777777$DD$O7$7ZZ7$7D8DMMMODNOO$OZ77$$77777$78DO$Z8$88$$Z8$$OZ$7")
    print("7777$$87D8N8$$DODNNNMMMN$ONO$D8Z8$NNMNN87ODMONNNMMMMNNND8$8MNNNNMNNNOD7O77777777777777777$OZ7777777777777777777777777777DO78777OZ7Z$DNDD8NNDZOOZ$D777777777$Z7ZZZ$DOZO$O$$$77$77")
    print("777777ZINNZD$8MD88MNDM8O$ZZ8ZNO8$8NDND8O7O$O8MMMNMMNNMNMZ7NNDND8NZDZ$8IO7777777777777777$O$O$$777777777777777777777777$ZZNO7777O7ODZO$OD8NIDZ8MOO$7$777777$777O7$7Z$$Z$DZZ8NOZ$7")
    print("77777778$D8N$8OMND$NMMM$Z$Z$7N777$NZ$$$$7OIO7NMMMMMMDN8O8ZNMDM8NMMMNN778777777777777777ZZZOZ7?$77777777777777777777777OOM$8$Z77ZOO$7$78NOONOZONZO7Z7$7777777$77$O$$IDIO88OD$$778")
    print("777777$ZDZMO7O8NMM8MMM$8$Z7778$7Z8NZO7777778NNDMNNMMNNDNZ$DNM8NMDN7OO7ID777777777777777$77$7Z$Z77777777777777777777777778O$O7777$O777Z$OZN8O$8D87$7777777777777$7Z887D$77ZZ7O8Z$")
    print("777777OZOOIZMO8$MMDMMNMMNZ777777$7877777777OMDMNNNMMNN8M$8MNNNNMNM8D$$Z777777777777777I777$7$Z8O777777777777777777777777788$77777Z777Z7$8I8D88IN7777777777777777$$$ZO$Z7N$O7Z7O8")
    print("777777$OO88OII8DNMMMMMNDN877777777777777777O8DMMNNN8DMM8NN$D8NNMM8$OD7$$777777777777IO$77777$ID7$77777777777777777777777$DOO77777777777Z$8ZZ7$Z7Z7777777777777777$ZZ7MDNZO787$7$")
    print("7777777777ZZ8$8O8MMMMMMOZZ7777777777777777778DMMDMMNNZDMD878OMMMNON78NZ$777777777777$O8OOZ$$7$O787777777777777777777777777777777777777777ZI77$$O7777777777777777777$878O$$O$777D")
    print("777777777777ZO8DN8DNMMN$NN77777777777777777$ODNDNMMMD8$DZZZD$$$87N8IO7D87777777777$77777$$O8O87IO$7777777777777777777777777777777777777777777$7$777777777777777777$77$Z$O7DD$$O8")
    print("7777777777777ZOMMM8MMMDN777777777777777777778DONNMMMOMZOZ887$IDON7$7Z7II777777777Z777777$777$ZII8I877777777777777777777777777777777777777777777777777777777777777O$7Z$$87NNN$$OZ")
    print("777777777777NM8N8MNMMNOZ$7777777777777777777$888MNNOON?$777Z777OIO$777$777777777$OOOZ$77777777$I878777777777777777777777777777777777777777777777777777777777777777777778OODND888")
    print("7777777777D7$OMMMMMMDMZ87O777777777777777777777MMMD$NMO7777777777$77777Z7777777Z$77$7ZOOZ$7777$$OIDI$777777777777777777777777777777777777777777777777777777777777777777788Z8$8ND")
    print("77777777777ONDNMNNMNOMM$7I777777777777777777I8ZNNM87ODI7777777777777777Z777777$777777777ZZOOZO$$ZIOIO7777ZO7777777777777777777777777777777777777777777777777777777777777Z8$OO$Z$")
    print("7777777777$$MNMMDOONNDO787Z777777777777777777INMMNNNMDOZ777777777777777777777OOZ$77777777777I$O777$7O$77O$ZO$$777777777777777777777777777777777777777777777777777777777$ZO8IZ8ON")
    print("777777777I8MZND8NZDNDND77O7777777777777777777NNNMNNDN88$777777777777777777777777$OOOO$77777$$7777$$787OO7$8ZD87777777777777777777777777777D8887777777777777777777777777IZ8IZ$Z7$")
    print("777777777777MDDNNMNN8OI7777777777777777777777O8N8OMDMNID$777777777777777777O777777777$$OOOO77777$8I7ZO$?ZZZO$$OD$7777777777777777777777777$ZDD877777777777777777777777777777787$")
    print("777777777777$8$MDM8NDN77777777777777777777II7DDDNN8M7ZI8$7777777777777I77IOOZ$777777777777$7$88ZZ7IZIN7ZZZ7~:I$7OZ7777777777777777777777I7OOZZZ77777777777777777777777777777ZZ77")
    print("7II777777I77ZINDNN8M87III777I77IIII7II7I7777II8D7NIMZO$OZI77III7777I77II7$7I7ZO88Z$$77777777777777I8IONOO$I,+7:7$7O777I777777777777777777$ND8OZ77777777777777777777777777777ZI$7")
    print("777777I77II77$$88N88ZI7IIIIIIIIII77IIIIIIIIIII$I7IN8I$77ZZ$IIIIII7I7I7777777777II77ZZO8Z$Z$77777$$IO7OOZ:I:7=7I:+7$ZO$777I777777777777777I7Z$ZZ$77777777777777777777777777777777")
    print("I7IIIII7IIII777ZD$MIIIIIIIII7IIIIIIIIIIIIIIIII7III7OIZ77$777III7II7IIIIOOZ$77777777777III$O$O888787IIN$::,:,OOO:O:77$88$7I7I777II7777I777I$Z$Z$77777I777777777777777777777777777")
    print("IIIIIIIIIIIII77887?7IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIZZ7IIIIIIII7IIIIIIII7I7Z$ZOOOO777777777777777777O8$I:I~~~+?$:~=I,$$7O77II7I7IIII7I7II7I7ZZO$7I7777777I77I77777777777777777777")
    print("IIIIIIIIIIIIII7?DN7IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII777777777777777Z$Z8N8DOZI+7II7O7?+,I88?$ZZZ=ZZZO~I7$DD$I77IIIIIIIII77I$OZO$77777IIII77I77II7I777777777777777")
    print("IIIIIIIIIIIIIIIO?ZO7IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIZOODDDDZI++++I77$$$$$$$7$$$$ZZ87~~:OOZ$$,DNDD$$$ZZO,$7$8D77II7IIIIIII777$7Z$7777II77I7777I77IIIII777II77I7777")
    print("IIIIIIIIIIIIIII7IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII$$$$777777$$$$$$$$$$$$$$$$$$ZO+?~:OZ$$$7I88DN$$$$$$ZI:$$78Z7IIIIIIIIIII$7$Z7$IIIIIIIIIIIIIIIII7IIIIIIIIII77II")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII7$$$$777777$$77$777777$$IZ7:::OZ$7?:7=,8ZND==$77$$$O:+7$$877IIIIIII7I$ZZO$$IIIIIIII7777IIIIIIIIIIIIII7IIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII777777$$7=~:?$7+::====OO7?:~OZ$$+?I7:,8OD8=,DNN87$$$Z,$7$DO$7IIIII7IZOZZO$Z$Z$77III77IIIIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII=:~~:~~==:$OID?D8?7:~,O7I?:?Z$77:8DDD:,O$OD=,DDD87$$$$$?,7$7OO7III77ZZZZO$$7IIII777$ZZ$Z7IIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII~~==~~,:?=ZDID$NDIZ$,8I:=:OZ$$:+~88DD~,O$O8~,DDD$,$7$$$$$,+$$7OZZZZZZZ$$$Z$777777$ZZO$I8IIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII,:::~==:O7$D$D8NN$8ZO?=::ZZ$I~:,:,,,,:::~::~=+II7:~,$$7$$$Z,$7$$Z$ZZZ$77$Z$777I$$$OZZ$ZOIIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII~=~:,,:,OO?8ZD8D8ZZI==~ZZ$$::::~I++==:===~:::,,~~:===?I77$$Z=~$$Z$D$IO$ZIZ$7777ZOZZZZZZ7ZIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII?,:~~~~:,,::~==??7ZI=::OZ$7=~~+~~:~:,::,:::::,,,.,~=+?7$$ZZZ$Z$~+$$$+MOOOZ7Z77$$$OOOO7ZZ?8IIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII::~::=,+77~~=7~~:??~+OOI~,::=+I7$Z$$77777$$$$$$$$$77777777$$$$ZZZOZZ$+MOO$Z777Z$OOZO7ZZIZIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII:::~~~==~:,,,:~::++OZZ$$$77777777$$$$$$$$$$$$$ZZ:=~,==::::7$77$ZZZZO$Z$+$$O7$$$ZZOZ$Z$Z$IIIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII~~~:,:,,:~~~~=+~::~,~7:~==:~~:::~~=888O8888888O7~:::,:~::==:7$$$ZZZZO8Z8$7$$$ZZZZOOZZ=Z$?$IIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII?IIIIIII?I::,,::~====++~::::::~=+=~~=::::,::+OOOO88888888I~:::::::~:,+:+$$ZZZOZ$NIZ$7D7$$77$77?:O$IOIIIIIIIIIIIIIIIII")
    print("IIIIIIIIIIIIIIIIIIIIII?III?IIII?III?II?IIIIIII?I?IIIIIIII?I????II???I==~~~~+=~::,,:~:~~=+~:::::::~:~=~:+OOOOOO8O8OOOI~::~::=~:=~~+=+=$$ZZO8DZI7$$?Z8888NZI~IZ7OIIIIIIIIIIIIIIIII")
    print("II?II?I??I?I?II??II?????I?II???I?I??????III??????I???II?I?????????I?7::::,:::~==~~====~,,::=~~=====:=~:++I7$O8DNNNND8~+~==~??~=+,:~=+?~$$ZNZZ777ZZZZ$$$Z?7:=$$7IIIIIIIIIIIIIIIII")
    print("II?I??I???III?I??????????I?I?I?????????I?????????????????????????I?77~====+~~:::~:,::~==~=:++:::~,:,,:::888888DDDDD88::=~:~::~:::,::?~?~?OZ$$$7$OZZ$$$ZZ7=$+ZZ?7IIIIIIIIIIIIIIII")
    print("??I?I?????????????????????????????????????????????????????????????+??~:,:,:~~:=O8D8888:~~~:,,:,,::::~~:~88888DDDDDD8O~:::,:~~,~+:~~~===~?=$$$$7$ZZZ$$$$$$$~=ZZIOIIIIIIIIIIIIIIII")
    print("???????????????????????????????????????????????????????????????????8+====~:=:ZDDDDDDD88D:::=~~=+==+==~:=888888DDDDD8O~~~:==~=~++~==+~?~?~+$7Z7$$Z$$$$$$7$$$Z?Z7$IIIIIIIIIIIIIIII")
    print("????????????????????????????????????????????????????????????????????+:::,:~:ODDDDDD88888Z~~++~:~=~:~::~+8O88888DDDD8Z:=++++:~=::~::=?=?==+7I$I$$7~~:=+==+ZO$Z78IIIIIIIIIIIIIIIII")
    print("????????????????????????????????????????????????????????????????????+==~~+:7DDD8888888OD8~~::,:::,::,~~?OO8888DDDDD8Z:=~~::~:::::,::+~+~?~7ZII$Z~~+=::~=+:7=Z7???II???I?IIIIIIII")
    print("??????????????????????????????????????????????????????????+=????????~:~:::7ID88OZ77I?++:?.,~~,,:=~~=~::?OOO888DDDDD8$:::::::,~:,+~:=~+~?=?$Z7$7Z::::~~:+=~+~~Z8II??????IIII??III")
    print("?????????????????????????????????????????????????????I7$I7?~?I????I?=~~===~:8Z8$OIO=O:O:I=====~~++:~+:,::::::,::::,::~=::~:==:=+~==+~?=+~?OO7I7$~=::=~:==:?=+$$II???????I??II???")
    print("????????????????????????????????????????????????????$$?~??=~?=I+I???~:::::~:88DZD$8?O~O:7~~::~~::::::I7??I?+=+~:==,:::==~++=?~=+~~+=+~?~?~7I$$7$,,::,:~==I+~+7????????????????I?")
    print("????????????????????????????????????????????????????7+???I~=II?7IIII+~~=~~:$I+?===~~===??,:,,::::~,,=~::=::+=:=+===~+=:++:=~:=~::~::?~=+=?$$$Z$7:~==~~+==~~~~I???????????????I??")
    print("???????????????????????????????????????????????????$$$$$7?+~~=~=~~::::::::::,:::,::~,::=~::=~:~=~~====+~=+~=+::=:,~~::~::::,::::::~:==~?~+ZZZZ7Z:::::,:==:~=????????????????????")
    print("???????????????????????????????????????????????????7I+=~:::::::::::::~:::::~~~::~~~~~~~==~:==:::~::~:,,~:,::,:::,,,::::,:,,:,~~::~:~~++~+~Z$Z$7$:~~~~~=+=:~~++??????????????????")
    print("????????????????????????????????????????????????????=::~::~~::::~~~~~~~~~::~=~::~~:::::::::,,,,,,,,,,::,,:,,::,,:::~::~::~:~~:~~:~:,?====+Z$77$Z:~~~::~=$~:=~+??????????????????")
    print("???????????????????????????????????????????????????===::,,,:::,,,,::,,,::::::~::~~~==++++??I??II7777777$77$7$$$$7$$$7$77$$$$$$$$$$$$$$+=+~?=7$7$:,:::::+~?Z7?+??????????????????")
    print("??????????????????????????????????????????????????7$$77777IIIII?I?III?????+++==~~:::::,,,,,,,:,,::,::::~~~~====+++???III7777$$$$$$$ZI=$$$7,?ZI77~~::~::=?~?~=+??????????????????")
    print("???????????????????????????????????????????????????$ZZ$ZZO:OZI?$ZOOO$+=8Z~$$O=?$OOOOOOOO888OZ:?ZZ~~~~~=:~~~~======+++~+++~II77$$$Z:~+~~Z+~?$7Z$$.::,,::==+~?~+??????????????????")
    print("????????????????????????????????????????????????????ZOZ7:8~8~DD8888O8OO=7:=I$OOOOO888O8OOOOOOON:7:~=~~,8OOOOOOOOOOOO?:~~~~?+++?7$$~==+=O+=$77$7$=777777$~++=+=??????????????????")
    print("?????????????????????????????????????????????????????O88+=~:8OONNONO88OO:~~?88888O888ODNNNNN8ZD$~:+:~::OOOOOOZOZOOOO+:=~=:~?ZNNNND8ZO~~~=77$I$7$?77II??=$$$=+=??????????????????")
    print("?????????????????????????????????????????????????????OD??~:7$O8+???OOOOOI~:DNNNNNO888ODNNNNNOZDD~:~~~:,OOOZZOOZZOZOZ?:==~::+$NNNNNN$Z~~~+7Z$$Z$$??+==::7~I??$Z??????????????????")
    print("?????????????????????????????????????????????????????O7??~?+?DO???IOOOOO8:ZNNNNNNODD8ZDD8888ZZDD~:~:~::OZOOZOOOOOZZO+:=~~~:~:NNNNNNZ,=~~?I$7777Z,::::::~=OO==+??????????????????")
    print("?????????????????????????????????????????????????????Z????+??DZ???IOZOOOO~NNNNNNDZOO8ZNNMMMN$ZD8=:~:~:7NDDNNNNNNNNND7:~=~::~,NNNNDD::,~=+?I$77$$,::::::~~=?~+=??????????????????")
    print("?I???????????????????????????????????????????????????O?Z?I???8????7OZZZZZ=NNNNNNDZOOOZ7NNNNN$ZDO~:+:~::NNDNNNNNNNNDDI:~~~::~,DNNNDD~::~++?$777$$:::::::~~=7~++??????????????????")
    print("????I????????????????????????????????????????????????ZIZ7?I??8????$OZZZZZ~OZZOOOOZOZOO8ZNNNN$ZD$=~~~=::NNDNNNNNNNDDDI:==~::~:OO88N8~::=?=+77$$7$~::::::=~=7~=+??????????????I???")
    print("II?IIIII?????????????????????????????????????????????OID?+???$????ZOZZZZZ:ZZZZZZZZZZOZ$7NNNN$ZD:Z:=~::,NDDNNNNNNNDND?:==~::~:OO77D?:::==~?$$7$$7$:::::~~~+I~~=??????????????OO?I")
    print("IIIIIIIII?II?II?I?????I?I????????????????????????????87:?=I??$????$ZZ$ZZZ=$ZZZZZZZZZZO~$Z?NDZ+=O?:=~=:,DDDNNNNNNNNND+~==~::::Z777D?:::=~~?I$IIZ7$,::~:~~:Z8~~????????????I??DDII")
    print("IIIIIIIIII7II$OI?IIIIIIIIIII?I?II???I????????IIIII7ZZZ$~8:OOOOO$OZ$$77II,:ZZZZZZZZZOZZ=Z.~~~~=~~=:==:::N8DDDDNNNNNND+~:+~::::777$8I:::~~~+$7$II77I~:~:~~~~+~==???????????I?IO$I?")
    print("7IIII7I7$$ZOOOO$OII$O$OO7$II$$Z77IIIIIIIIIIIIIIIII77?I+:Z~Z?ON78+7=+I+?.Z,OZZZZZZZZZO$~,$:.ZIODO?~~~:::D8DDDDDNNDNDD=~=~~::~~77I7D+:::~~~+7Z$Z$$I$:~~::~~~+~+=?I???I???IIIII$III")
    print("O8OOOOZOOOO8OO8OOOZOOOO88OO$ZOZOO7IIIIIIIIIIIIIIII7==+?=7~O?ONIZ~?,~~::Z+7ZZZZZZZZZZO$:7~~=N$?O$+~~~~:~,::::~~=++??I=~~~~:::~777$D+:::~~~=$$7I7$7$~~~~~~~~+~+=IIIII??II?IIII$II?")
    print("88888O88888D88888$OO8ODZO8O$OD88OIIIIIIIIIIIIIIIIOI=++==?~Z78DZOI$=?:=:?7:ZZZZZZZZZZO7:+~::$?IOI~~:::::::,,,:::,::::~~?+~:::::::::::,:~~:=7$ZZ$7ZZ~~~:~~~:+~==77IIIIIIIIIIII$III")
    print("OD$8OD?788NDDOOD8D8NDDDD8NOOODDD8O8DOO$Z$ZOZZO7OD8~~~:::,:?$7?$77Z=,7:=$~~ZZZZZZZZZ=.+:=~:=87OOZ7777777$7$$$$$$$$$$$$$$777$$$$$$$$$$$$$~~~77?OZ7$7~~~:~=~++~=+I77II7II77I:7I$III")
    print("DDO8888O8O8O8O88OZOOOZOO8Z8~OZD$$7++I888ZOOI$ZI=IDZOZ,~:,=II7777?:I.++I~:=ZZZZZZOZ$Z$77I?:.I=ZZO=:+~===~=+=~~~===~:~::~~~~::=~::=~:~~:7==~777Z$$7$~~=~~=7=+?~=777Z8O87$7O$ZI88I7")
    print("N88DD88O8O888D8ND88OD8D8OOOO8DO88ZDON88DOOO88ZDDDZZZZ,:,:~::::,~$.+=??=:?=$$$ZO8O8?Z$,:,~+OZIII7=:::::::::::~~==+???I7II~::=??$?=?+==:=~=:7$$$Z$7$~~~~~++=====OO88OO888O8$88OO88")
    print("N8NDD8888D8DMDNNDDNMNN8N8DNNNNDD8DZDDODDN88D8ND88Z77$,:,:::~+?7??$$I?~+.:OOOOOOOOIO$$:::=$77II?+=::::~~==++????????+=~~~::::::::::,,:,~?==Z$Z$Z$Z$:::::=++===:~~OZZZ7OOO$$DZZO8$")
    print("MNODMNND8DDDNMNNNO8NM8NDDNMNMNDMN8N8N8DD8N8NDDD88$7=~,::::::~::,~:~~~7I:OOOOOOO88D?+I::::=?I7777:~~~~=++??I77$$$77I??++=:::~:::,,,,,,:~~7~7$7$$ZO$===:=??I??I=~~~=7ZO88O8$D8I?O8")
    print("DZO8MNM88O8ZNM8ZZMMNZDMMZ$8MNDONNNM$OZOODMMOO8Z$$7+=~::~,~:$I~~:~~~,$7OOOOZOOOO88DD+I:~~:::::::::::::::~~~~::::::~====~~~~::::::,:,:~:~:~,I$ZZ$$$$==~~~=+~~++~~~:?~~=Z88D$O888OO")
    print("OOZDD8OOO88D8Z8O8DDDOZNDO$O8DNO$$OZZZ$$$O$D8$7$$7?+=~::::::~~~:=~,+:+OOOO8888DD88DN=$:~=::::::::::::::~~~+888DDD~:~~~:::~~::::::::::=:=:+:7$Z7$$I$===~~++=~==~~~~~~~+=~I~$7$N8$Z")
    print("8$7$$$$$7Z$$$ZZ$$8Z$7O8$$7$$D7$Z$Z$7$ZOZOOZ7ZZ777+===::::~:::~=,I:I$O88DDD88OZZ$$D8=I::::,::::::~~~~~==+~?88ODDD~:::::::~~::::::::::~:=I+~7$77$7ZZ===~~+==~~~~~~~~~~~~~~=~~788$$")
    print("$$$$$$$$$$$$Z$$$7$77I$7777777777$$$$77$$$$777$$777?++:::~~~~~+I7~8O8DOZZ$77I7$$$DM$~7:~~::::~~~~~=====~~~I8O88OD~::~~~~~~~:,::,:::::~::=+I77$$$$7$=++~~+++~~~=~~~~~~~~~~=7~?NNI7")
    print("II7II$7IIIIIIIIIIII7IIII$I77$7777777IIIIIIIIIII?8ZZ??~~~:,,,,:=DD8O$7777$$ZZOOOO8N$~I:~~:~~====~~~~~~::~~7ZO8DZN~~~~::=:~~:=~~:~~:I+=~~~+?$$77$$Z$I$II=+=+==+?7$?II?+~+=~8$NNNMI")
    print("I7$$77$77$77777$$77III7II7IIIIIIIIIIII7$IIII77IIIIII??++$$ZZ$Z$88OZ$Z77I77$$$$$OODO+I:::~~===~~~~::::::~::~~::::=~:::~?~~~:+=++===+I====8O77$Z$77IO$7++~=ZZ7I$ZZ77I777$7I77$D88I")
    print("77777$$$77IIIIIII7I$777I7IIIIIIIIIIIIIIIIIIIIIIII7777$$77II77777777777777?77I$$$Z8N??:::I7IIIII??7$$7$$7I?==:::~=:~~~~~=~=~~~~~~~~::~=~?NO777I7I7$8I??$7I?II77II7IIIIIIIIIII8OZI")
    print("7I77IIII7I77III$$I??IIIIIIIIIIIIII7IIIIIIIII77777III7IIIIIIII7I7777777I77777777$77$7ZII??IIIIIII777Z$7III77$$$ZZ8OOOOOZZOOIIII777III7777$$7777777$7777$I7IIII7IIIIIIIII?7?II88Z7")
    print("II7II77777I7I7III7II7II7777I77Z77777I7I7I77$$IIIIIIIIIIII7IIIIIIIIIIIIIIIIIII7777I777III7I?IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII$III7I7II7I77I77I777I$777I77777I77I7IIII7IIII8O77D8O$")
    print("")
    print("")
    print("")
    print("1. Type 1 and hit enter to end game")
    menu = int(input(""))
    if menu == 1:
        print("Congratulations on completing the game!")
    else:
        quit()

main()
