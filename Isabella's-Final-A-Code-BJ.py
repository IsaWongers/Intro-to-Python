class Player:
    def __init__(self,n,w):
        self.name = n
        self.timeswon = w

    def __str__(self):
        return(self.name+" has won: "+str(self.timeswon))

class Card:
    def __init__(self,r,s):
        self.rank = r
        self.suit = s # how does ne link this to makeADeck()?

    def __str__(self):
        return(self.rank,self.suit)
    
class Deck:
    def __init__(self):
        ranks = ["♣","♦","♥","♠"]
        suits = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        deck = []
        self.cards = [deck.append(Card(suit, rank) for suit in suits for rank in ranks)]

    def shuffle(self):
        import random
        shuffled = random.shuffle(self.cards)
        return(shuffled)

deck = []
shuffled = deck.shuffle()

def main():
    instructions()
    win = False
    bust = False
    player1 = Player(input("What's your name? "), 0)
    hand1 = []
    hand1 = dealAHand(shuffled)
    print("This is your hand: "+str(hand1))
    bjTotal = 0
    for c in hand1:
        bjTotal += create_BJValue_LookUp(c)
    # bjTotal = calcsum(values)
    print(player1.name+", your total is: "+str(bjTotal))
    win = wincheck(bjTotal,player1,win)
    bust = bustcheck(bjTotal,player1,bust)
    hand1 = hitOrStay(hand1,bjTotal,shuffled,win,bust,player1)
    print(player1)

def instructions():
    print("You are given two random cards to start with. ")
    print("The goal of Blackjack is to get to 21 with the cards you are dealt. ")
    print("If you get more than a value of 21, then you bust and lose. ")
    print("You can add more cards by hitting or not for the round by staying. ")
    print("Ace is 1. Jacks, Queens, and Kings are worth 10 each. ")

# import random
# def makeADeckOf52():
    
    # cardSuits = ["♣","♦","♥","♠"]
    # cardRanks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    # deck = []
    
    # for s in cardSuits:
        # for r in cardRanks:
            # deck.append(r+s)

    # random.shuffle(deck)
    
    ### you can comment out the next three print lines after you run this once   
    # print(deck)          
    # print()
    # print(sorted(deck))  #easier to check if all cards are in the deck but is alphabetical
    # return(deck)

def create_BJValue_LookUp(c):
    #assume card is in this format: A♣ , 10♥

    rank = c[:len(c)-1]
    # print(rank)
    specialValues = {"A":1, "J":10,"Q":10,"K":10}
    if rank in specialValues:
        bjValue = specialValues[rank]
    else:
        bjValue = int(rank)
    return(bjValue)

def dealAHand(shuffled):
    h = []
    h.append(shuffled.pop(0))
    h.append(shuffled.pop(0))
    return(h)

# def cardLookUp(hand1): # I DON'T NEED THIS- it's nice to look at tho
    # try to get individual values here
    strhand1 = ", ".join(hand1)
    values = []
    alpha = ""
    for shape in strhand1:
        if shape == ["♣","♦","♥","♠"]:
            alpha += shape
        elif shape == "J":
            shape = 10
            values.append(shape)
        elif shape == "Q":
            shape = 10
            values.append(shape)
        elif shape == "K":
            shape = 10
            values.append(shape)
        elif shape == "A":
            shape = 1
            values.append(shape)
        elif shape == 10:
            shape = 10
            values.append(shape)
        elif shape.isnumeric():
            shape = int(shape)
            values.append(shape)
    return(values) # THIS ISN'T NEEDED!!

# def calcsum(values):
    # add up the values here
    total = sum(values) # lol i don't need this anymore
    return(total)

def hitOrStay(hand1,bjTotal,deck,win,bust,player1):
    # this is where the game is played
    keepGoing = 'y'
    while bjTotal < 21 and keepGoing == 'y' and win == False and bust == False:
        addOrNot = input("Hit or stay? [H/S] ")
        addOrNot = addOrNot.capitalize()
        if addOrNot == "H":
            hand1.append(deck.pop(0))
            print(hand1)
            bjTotal = 0
            for c in hand1:
                bjTotal += create_BJValue_LookUp(c)
            # bjTotal = calcsum(values)
            print(player1.name+", your total is: "+str(bjTotal)) # this might be a problem
        else:
            hand1 = hand1
        wincheck(bjTotal,player1,win)
        bustcheck(bjTotal,player1,bust)
    return(hand1,bjTotal)

def wincheck(bjTotal,player1,win):
    if bjTotal == 21:
        win = True
        player1.timeswon += 1
        print("Congrats! You won...bragging rights! ")
    else:
        win = False
    return(win)

def bustcheck(bjTotal,player1,bust):
    if bjTotal > 21:
        bust = True
        player1.timeswon += 0
        print("Yeah you lost. ")
    else:
        bust = False
    return(bust)

main()
