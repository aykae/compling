import json
import csv

def serializeWordsPos():
    pos_dict =  {}
    with open("words_pos.csv", "r") as posFile: 
        reader = csv.reader(posFile)
        for row in reader:
            pos_dict[row[1]] = row[2]
    
    with open("words_pos.json", "w") as posJson:
        json.dump(pos_dict, posJson)

#serializeWordsPos()

