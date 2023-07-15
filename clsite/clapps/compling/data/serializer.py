import json
import csv

def serializeWordsPos():
    posDict =  {}
    with open("words_pos.csv", "r") as f: 
        reader = csv.reader(f)
        for row in reader:
            posDict[row[1]] = row[2]
    
    with open("words_pos.json", "w") as f:
        json.dump(posDict, f)

def serialize10kWords():
    wordList = []
    with open("raw/10kwords.txt") as f:
        for line in f.readlines():
            wordList.append(line.strip())

    with open("10kwords.json", "w") as f:
        json.dump(wordList, f)

def generatePosToWord():
    ptwDict = {}
    with open("words_pos.json") as wp, open("10kwords.json") as tk:
        wpDict = json.load(wp)
        tkList = json.load(tk)
        for w in tkList:
            if w in wpDict.keys(): #Flip mapping from POS -> Word
                if wpDict[w] in ptwDict.keys():
                    ptwDict[wpDict[w]].append(w) 
                else:
                    tempList = []
                    tempList.append(w)
                    ptwDict[wpDict[w]] = tempList
    
    with open("pos_to_word.json", "w") as f:
        json.dump(ptwDict, f)


#serializeWordsPos()
#serialize10kWords()
generatePosToWord()

