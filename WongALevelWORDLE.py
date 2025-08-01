# this program is to make a WORDLE
def instructions():
    print("This is the Walmart version of WORDLE. ")
    print("The rules of the game are the same as the ones of NYTimes. ")    
    print("You are given 5 tries to guess a word that is 5 letters long. ")
    print("NO DOUBLE lETTER WORDS!! ")

def main():
    instructions()
    # insert the list of words
    f = open("wordleWords.txt","r")
    lines = f.readlines()
    f.close()

    processedwords = []  # these are where the words sit

    for line in lines:
        line = line.rstrip()
        words = line.split(' ')

    for word in words:
        word = word.capitalize()
        processedwords.append(word) # puts them all in a list
        
    # print a grid
    grid = [['_','_','_','_','_'],
            ['_','_','_','_','_'],
            ['_','_','_','_','_'],
            ['_','_','_','_','_'],
            ['_','_','_','_','_'],]
    prettyPrintGrid(grid)

    # getting the answer
    answer = list(correctwordle(processedwords))
    secret = []
    for letter in answer:
        answer = letter.upper()
        secret.append(answer)

    # print(secret) was just to check

    getGuessResult(secret,grid)

def prettyPrintGrid(g):
    for row in g:
        for col in row:
            print(col, end = ' ')
        print()

def correctwordle(processedwords):
    # make a correct word
    import random
    correct = random.choice(processedwords)
    return(correct)

def getGuessResult(secret,grid):
     # playing the game
    turns = 0
    finguess = ' '
    result = ' '
    count = 0
    while turns < 5 and finguess != secret:
        result = []
        guess = list(input("What's your guess? "))
        finguess = []
        for item in guess:
            guess = item.upper()
            finguess.append(guess)
        n = 0
        for item in finguess:
            if item == secret[n]: # make this go thru all the letters
                item = "\033[42m"+item+"\033[0m"
                result.append(item) # make it green
            elif item in secret:
                item = "\033[43m"+item+"\033[0m"
                result.append(item) # make it yellow
            else:
                item = "\033[100m"+item+"\033[0m"
                result.append(item) # make it grey
            n += 1
        reportCorrectLetters(finguess,secret)
        # print the rest of the grid here
        grid[turns] = result
        for row in grid:
            for col in row:
                print(col, end = ' ')
            print()
        # print(grid)
        turns += 1
        count += 1
        finale(finguess,secret,count)

def reportCorrectLetters(finguess,secret):
    letters = []
    for item in finguess:
        if item in secret:
            letters.append(item)
    print("The correct letters are ", letters)

def finale(finguess,secret,count):
    if finguess == secret:
        print("Congrats!! You got it in ",count, "tries! ")
    else:
        print("Oh...better luck next time. You did not win. ")

main()

# used words = grown, trial, train (train was correct)