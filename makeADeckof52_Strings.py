import random
def makeADeckOf52():
    #input: none
    #output: a list of 52 strings
    #process: pair the 4 suits with the 13 card rank values
    
    #modeling the 52 cards:
    #A-K of clubs,diamonds, hearts, spades
    
    cardSuits = ["♣","♦","♥","♠"]
    cardRanks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    deck = []
    
    for s in cardSuits:
        for r in cardRanks:
            deck.append(r+s)


    random.shuffle(deck)
    
    ### you can comment out the next three print lines after you run this once   
    print(deck)          # just to make sure deck got made
    print()
    print(sorted(deck))  #easier to check if all cards are in the deck but is alphabetical
    return(deck)

makeADeckOf52()
