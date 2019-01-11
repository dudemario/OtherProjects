'''
Created on Mar 10, 2017

@author: Victor Sun
'''


currentState = 1            #Stage 1 or 2
drawersCheck = False        #If drawers have been opened
drawersDestroyed = False    #If drawers have been destroyed
hammer = False              #If hammer has been obtained
matchbox = False            #If matchbox has been obtained
win = False                 #If player has won the game
lose = False                #If player has lost the game
finish = False              #If player has quit the game
time = 0                    #Clock
hurt = 0                    #Injury counter
hintStage = 0               #Number reference for next hint to be displayed

#Recieves input from player using a predefined message.
#Checks if input only contains letters and spaces.
#Returns the input to whatever called the method
def getInput(description):
    response = "0"
    response = raw_input(description)   #Recieves input as a string
    print
    print
    test = response                     #Stores input in a temporary variable

    #Removes spaces from word
    for x in test:                      #Runs through each character in 'test'
        i = test.index(x)               #Finds index of the character in the word
        if x == " ":                    #Checks if character is a space
            test = test[:i] + test[i+1:]#Rewrites test but without that space
            
    while test.isalpha() == False:      #After removing all the spaces, checks if the word has any other characters that aren't letters
        print "Invalid Input."           #Prompts user
        print
        print
        response = raw_input(description)   #Restart input process..
        print
        print
        test = response
        for x in test:
            i = test.index(x)
            if x == " ":
                test = test[:i] + test[i+1:]
    return response

#Recieves input as an action.
def getAction():
    return getInput("What would you like to do?\n")

#Recieves input as an item to use hammer/fists on.
def getItem():
    return getInput("But on what?\n")

#Prints description of the first stage: room.
def lookaround1():
    global time
    global hintStage
    print "The room is a complete square, with a door on one side and a window on the other."
    print "It appears that the window has been painted over."
    print "In the room, there's a set of drawers and a bed."
    if hintStage < 1:
        hintStage = 1
    time += 10

#Same as above but for second stage: hallway
def lookaround2():
    global time
    global hintStage
    print "Looks like a hallway, branching off to the right or left."
    if hintStage < 7:
        hintStage = 7
    time += 10

#Checks if drawers are broken or have already been checked, if not, then it prints the drawer's contents.
def lookindrawers():
    global time
    global drawersDestroyed
    global drawersCheck
    global hintStage
    if drawersDestroyed:
        print "It's broken, too bad..."
    else:
        if drawersCheck:
            if hammer:
                if matchbox:
                    print "There's nothing left in the drawers."
                else:
                    print "Inside the drawers, you see a matchbox."
            else:
                if matchbox:
                    print "Inside the drawers, you see a hammer."
                else:
                    print "Inside the drawers, you see a matchbox and a hammer."
        else:
            print "Inside the drawers, you see a matchbox and a hammer."
            drawersCheck = True
            time += 5
            hintStage = 2

#Checks if player already has a hammer, if not, checks if player has opened the drawers, which aren't destroyed, and gives the player a hammer.
def pickuphammer():
    global time
    global drawersCheck
    global hammer
    global hintStage
    if hammer:                      #Checks if player has hammer
        print "You already have the hammer."
    else:
        if drawersCheck:            #Checks if drawers have been opened
            if drawersDestroyed:    #Checks if drawers have been destroyed
                print "Drawers are broken... Too bad..."
            else:
                print "You pick up the hammer. "
                hammer = True       
                time += 5
                if hintStage == 2:  #Sets next hint according to if other item (matchbox) has also been picked up
                    hintStage = 3   #Still missing matchbox
                else:
                    hintStage = 4   #Already have matchbox
        else:
            print "There doesn't seem to be a hammer around."
            time == 10

#Same as above but for the matchbox.
def pickupmatchbox():
    global time
    global drawersCheck
    global matchbox
    global hintStage
    global drawersDestroyed
    if matchbox:
        print "You already have the matchbox."
    else:
        if drawersCheck:
            if drawersDestroyed:
                print "Drawers are broken... Too bad..."
            else:
                print "You pick up the matchbox. "
                matchbox = True
                time += 5
                if hintStage == 2:
                    hintStage = 3
                else:
                    hintStage = 4
        else:
            print "There doesn't seem to be any matchboxes around."
            time == 10

#Increases time by 30 min.
def wait():
    global time
    print "You wait 30 min..."
    print "Nothing seemed to happen."
    time += 30
    
#Tells the player that the door is locked.
def opendoor():
    global hintStage
    global time
    print "The door is locked."
    time += 10
    hintStage = 5
    
#Allows player to use the matchbox if obtained, but to no avail.
def usematchbox():
    global time
    global matchbox
    if matchbox:
        print "Nothing to use it on."
        time += 10
    else:
        print "If you only had a matchbox..."
        time += 10
    time += 10
    
#Same as above but if hammer is obtained, recieves input on what to use it on
def usehammer():
    global time
    global hammer
    if hammer:
        checkItemInput("Hammer", "Door", "Drawers", "Window", "Bed")
        time += 5
    else:
        print "If you only had a hammer..."
        time += 10
    
#Same as above but no need to check if player has fists.
def usefists():
    global time
    time += 10
    checkItemInput("Fists", "Door", "Drawers", "Window", "Bed")

#List of hints to be printed depending on the current situation.
hints = {0 : "Sometimes it's a good idea to Look around, at your surroundings and see what's there.",
         1 : "Those drawers look pretty suspicious, maybe you should Look in the drawers.",
         2 : "Instead of just looking at them, how about trying to Pick up the [item], make sure to be specific.",
         3 : "The other item might come to good use too.",
         4 : "How about trying to Open the door?",
         5 : "Hmm, could you maybe Use [an item]?",
         6 : "Again, looking around might help.",
         7 : "You can either Go left, or Go right, choose one.",
         
}

#Displays hint depending on current situation.
def showhint():
    global time
    global hintStage
    print hints[hintStage]
    time += 5
    
#Allows player to quit the game
def quitgame():
    global finish
    finish = True

#Changes state to hallway and tells player.
def hammerdoor():
    global time
    global currentState
    global hintStage
    print "Door breaks, and you enter the next room."
    print "The door closes behind you..."
    hintStage = 6
    currentState = 2
    time += 5

#Breaks drawers, making its items unavailable anymore
def hammerdrawers():
    global time
    global drawersDestroyed
    print "Look what you done, there's no way you're going to get anything out of it anymore."
    drawersDestroyed = True
    time += 10

#Prints description of what's behind window and makes player hurt
def hammerwindow():
    global time
    global hurt
    print "You see a steel wall. Looks like this isn't the way out."
    print "Also, some of the glass hits you, luckily it's only a scratch."
    time += 10
    hurt += 1

#Prints result of using hammer on bed
def hammerbed():
    global time
    print "Ok, now was that really necessary?"
    time += 10

#Gives player description and switches stage
def goleft():
    global time
    global currentState
    global hintStage
    print "You see a door at the end of the hallway."
    print "You open the door and enter the room."
    print "Unfortunately, you take a whiff of some kind of gas and faint."
    print "You wake up on a wooden bed."
    print "The room looks familiar."
    time += 10
    currentState = 1
    hintStage = 0

#Checks if player has matchbox. If yes, puts user in win position, if not, puts in lose position
def goright():
    global matchbox
    global win
    global lose
    if matchbox:
        print "It looks dark so you pull out your matchbox and light a match."
        print "You see people ready to ambush you but with your expert mobility, you avoid them."
        print "The exit is at the end of the hall and you escape with your life."
        win = True
    else:
        print "It looks dark but you go anyway."
        print "Unfortunately for you, you get ambushed along the way."
        lose = True

#List of action methods for the first stage
functions1 = {0 : lookaround1,
              1 : lookindrawers,
              2 : pickuphammer,
              3 : pickupmatchbox,
              4 : wait,
              5 : opendoor,
              6 : usematchbox,
              7 : usehammer,
              8 : usefists,
              9 : showhint,
              10 : quitgame,
}

#Same as above but for the second stage
functions2 = {0 : lookaround2,
              1 : goleft,
              2 : goright,
              3 : showhint,
              4 : quitgame,
}

#List of actions that can be done with hammer
hammerActions = {0 : hammerdoor,
                 1 : hammerdrawers,
                 2 : hammerwindow,
                 3 : hammerbed,
}

#Recieves the stage number and a list of strings to compare the input from player to a list of valid action inputs.
#With those variables on hand, recieves input from player and checks it to the valid inputs.
#If valid, calls respective function.
#If not valid, tells player and repeats input process.
def checkActionInput(stage, *args):
    global time
    end = False
    test = getAction()      #Recieves input
    for x in args:          #Loops through each valid action
        if test == x:       #Checks if input equals action
            if stage == 1:  #Checks current stage
                functions1[args.index(test)]()  #Runs respective functions
            else:
                functions2[args.index(test)]()
            end = True      #Ends function
    while end == False:     #Loops until valid action
        print "You wonder what that could mean..."
        print
        print
        time += 10
        test = getAction()
        for x in args:
            if test == x:
                if stage == 1:
                    functions1[args.index(test)]()
                else:
                    functions2[args.index(test)]()
                end = True

#Same as above but for checking what the player wants to use the hammer or their fists on.
def checkItemInput(arg1, *args):
    global time
    global hurt
    end = False
    test = getItem()
    for x in args:
        if test == x:
            if arg1 == "Hammer":
                hammerActions[args.index(test)]()
            else:
                print "You hurt yourself, how silly of you."
                hurt += 1
                time += 10
            end = True
    while end == False:
        print "You wonder what that could mean..."
        print
        print
        time += 10
        test = getItem()
        for x in args:
            if test == x:
                if arg1 == "Hammer":
                    hammerActions[args.index(test)]()
                    
                else:
                    print "You hurt yourself, how silly of you."
                    hurt += 1
                    time += 10
                end = True

#Controls the game after being initialized.
#Calls function for getting input
#After the corresponding function runs (within checkActionInput), checks if game has ended due to time, injury, quit, change stage, win, or loss
#If any are true, prints to player and ends game or changes stage.
#If game has ended, also asks player if they want to play again.
#If yes, clears all variables and restarts game.
def stage1():
    global currentState
    global drawersCheck
    global drawersDestroyed
    global hammer
    global matchbox
    global win
    global lose
    global finish
    global time
    global hurt
    global hintStage
    end = False
    while end == False:         #Checks if stage has ended in some way
        print
        print
        
        #Recieves input and calls function
        checkActionInput(1, "Look around", "Look in the drawers", "Pick up the hammer", "Pick up the matchbox", "Wait", "Open the door", "Use matchbox", "Use hammer", "Use fists", "Show hint", "Quit game")

        if time >= 240:         #Checks if time has passed 4 in-game hours
            print "All of the sudden, the steel wall behind the window opens and a horde of hungry tigers devour you."
            print "Too bad, Game Over."
            end = True
        if hurt == 4:           #Checks if player has taken 4 injuries
            print "You have taken too many injuries and die of exhaustion."
            print "Too bad, Game Over."
            end = True
        if finish:              #Checks if player has chosen to quit
            print "Come back next time."
            end = True
        if currentState == 2:   #Checks if player has advanced to second stage
            end = True
    if currentState == 2:
        stage2()                #Calls this function again but will run differently because of new current stage
    else:
        print
        print
        print
        response = raw_input("Would you like to play again?\n")     #Asks user if they want to play again
        if response == "Y" or response == "Yes":
            #Resets variables
            currentState = 1
            drawersCheck = False
            drawersDestroyed = False
            hammer = False
            matchbox = False
            win = False
            lose = False
            finish = False
            time = 0
            hurt = 0
            hintStage = 0

            #Intializes game again
            main()

#Same as above but for stage 2
def stage2():
    global currentState
    global drawersCheck
    global drawersDestroyed
    global hammer
    global matchbox
    global win
    global lose
    global finish
    global time
    global hurt
    global hintStage
    end = False
    while end == False:
        print
        print
        checkActionInput(2, "Look around", "Go left", "Go right", "Show hint", "Quit game")
        if time >= 240:
            print "All of the sudden, the steel wall behind the window opens and a horde of hungry tigers devour you."
            print "Too bad, Game Over."
            end = True
        if hurt == 4:
            print "You have taken too many injuries and die of exhaustion."
            print "Too bad, Game Over."
            end = True
        if win:
            print "Congratulations, you have WON!"
            end = True
        if finish:
            print "Come back next time."
            end = True
        if lose:
            print "Too bad, you lost."
            end = True
        if currentState == 1:
            end = True
    if currentState == 1:
        drawersCheck = False
        hintStage = 0
        stage1()
    else:
        print
        print
        print
        response = raw_input("Would you like to play again?\n") 
        if response == "Y" or response == "Yes":
            currentState = 1
            drawersCheck = False
            drawersDestroyed = False
            hammer = False
            matchbox = False
            win = False
            lose = False
            finish = False
            time = 0
            hurt = 0
            hintStage = 0
            main()
            

#Initializes the game, prints to the player
def main():
    print "Some tips for this game:"
    print "All commands will start with an Uppercase letter and every other letter afterwards is lower case. (Eg: Start here)"
    print "If you would like a hint on what to do next, type: Show hint"
    print "Good Luck!"
    print
    print
    print 
    print "You wake up on a wooden bed, feeling groggy."
    print "You don't know where you are."
    print
    stage1()

#Game starts here
main()
