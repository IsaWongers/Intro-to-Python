def create_BJValue_LookUp(cardStr):
    #assume card is in this format: A♣ , 10♥

    rank = cardStr[:len(cardStr)-1]
    # print(rank)
    specialValues = {"A":1, "J":10,"Q":10,"K":10}
    if rank in specialValues:
        bjValue = specialValues[rank]
    else:
        bjValue = int(rank)
    return(bjValue)

#you can remove the next line once you understand this code
# it's just to test
print(create_BJValue_LookUp("10♣"))
print(create_BJValue_LookUp("A♣"))
print(create_BJValue_LookUp("7♥"))

    
