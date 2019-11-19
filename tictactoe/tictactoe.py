import os
cls = lambda: os.system('clear')

playerSide = ''
gameFinished = False
roundFinished = False
marks = {"1":" ", "2":" ", "3":" ","4":" ", "5":" ", "6":" ","7":" ", "8":" ", "9":" "}
ver = "   |   |   "
hor = "___|___|___"

def starTTT():
    cls()
    global gameFinished
    while gameFinished == False:
        prepareStart()
        startGame()
        celebration()
    
def drawTable():
    row3 = " "+marks["7"]+" | "+marks["8"]+" | "+marks["9"]+" "
    row2 = " "+marks["4"]+" | "+marks["5"]+" | "+marks["6"]+" "
    row1 = " "+marks["1"]+" | "+marks["2"]+" | "+marks["3"]+" "
    print(ver)
    print(row3)
    print(hor)
    print(ver)
    print(row2)
    print(hor)
    print(ver)
    print(row1)
    print(ver)
    
def prepareStart():
    global gameFinished
    global playerSide
    side = ''
    while side == '':
        prompt = input("Please select side (X or O): ").upper()
        if prompt == "X" or prompt == "O":
            side = prompt
        else:
            print("Please select 'X' or 'O'")
    playerSide = side
    gameFinished = False
    drawTable()
    
def startGame():
    global roundFinished
    while roundFinished == False:
        makeTurn()
        cls()
        drawTable()
        calculateResult()
        
def passTurn():
    global playerSide
    if playerSide == 'X':
        playerSide = 'O'
    else:
        playerSide = 'X'
        
def makeTurn():
    global playerSide
    print("Player '" + playerSide + "' please make your turn:" )
    cell = input("Please select cell: ")
    marks[cell] = playerSide
    
def calculateResult():
    global roundFinished
    global marks
    if marks["1"] == marks["2"] == marks["3"] and marks["1"] != " ":
        roundFinished = True
    elif marks["4"] == marks["5"] == marks["6"] and marks["4"] != " ":
        roundFinished = True
    elif marks["7"] == marks["8"] == marks["9"] and marks["7"] != " ":
        roundFinished = True
    elif marks["1"] == marks["4"] == marks["7"] and marks["1"] != " ":
        roundFinished = True
    elif marks["2"] == marks["5"] == marks["8"] and marks["2"] != " ":
        roundFinished = True
    elif marks["3"] == marks["6"] == marks["9"] and marks["3"] != " ":
        roundFinished = True
    elif marks["1"] == marks["5"] == marks["9"] and marks["1"] != " ":
        roundFinished = True
    elif marks["7"] == marks["5"] == marks["3"] and marks["7"] != " ":
        roundFinished = True
    else:
        passTurn()
    
def celebration():
    global playerSide
    print(playerSide + " wins!")
    repeat()
    
def repeat():
    global gameFinished
    global roundFinished
    global marks
    repeatGame = input("Would you like to repeat? (Y/N): ").upper()
    if repeatGame == "Y":
        roundFinished = False
        marks = {"1":" ", "2":" ", "3":" ","4":" ", "5":" ", "6":" ","7":" ", "8":" ", "9":" "}
        cls()
    else:
        gameFinished = True
        print("Thanks for playing!")

if __name__ == "__main__":
    starTTT()