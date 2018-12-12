def hamming_distance(mainW, helpW):
    distance = 0
    if len(mainW) > len(helpW):
        helpW = helpW.ljust(len(mainW))
    elif len(mainW) < len(helpW):
        mainW = mainW.ljust(len(helpW))
    for a, b in zip(mainW, helpW):
        if a != b:
            distance=distance+1
    #print("Distance od "+str(mainW) + " i "+str(helpW)+" to: " +str(distance))
    return distance


mainWord = input()
helpWordsAmmount = int(input())
if helpWordsAmmount == 0:
    print("BRAK PODPOWIEDZI")
else:
    helpWords = []
    goodHelpWords = []
    maxDistance = 31

    for i in range(helpWordsAmmount):
        helpWord = input()
        helpWords.append(helpWord)
    
    for i in helpWords:
        distance = hamming_distance(mainWord, i)
        if maxDistance > distance:
            goodHelpWords.clear()
            goodHelpWords.append(i)
            maxDistance = distance
        elif maxDistance == distance:
            goodHelpWords.append(i)
    
    for i in goodHelpWords:
        print(i)