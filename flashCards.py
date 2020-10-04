import Dictionary.dictionary as dictionary
import os
import sys
import subprocess
import numpy as np

#constants
numberOfTotalDays = 30
clearThreshold = 4
sessionWordThreshold = 1000

days = [12  , 15]

words = {}

numberOfWords = 0


#setting words


if type(days) is not list:
    days = np.arange(1, numberOfTotalDays+1).tolist()


for day in days:

    dayDict = dictionary.days[day-1]
    numberOfWords += len(dayDict.keys()) 

    for item in dayDict.keys(): 
        words[item] = dayDict[item]



randomIndexes = np.arange(numberOfWords)
np.random.shuffle(randomIndexes)




#functions

def doSession(indexes, words):

    global sessionWordThreshold
    global clearThreshold

    numberOfWords = len(indexes)

    print("\n\n")

    print("# of words at total : ", numberOfWords)

    print("\n\n")        

    numberOfYes = 0
    indexesFailed = []



    for i, j in enumerate(indexes):

        if(i == sessionWordThreshold):
            print("\n \n End of session, go take a respite \n \n")
            print("Stats : ", numberOfYes, " yes in ", numberOfWords)
            print("Days : ", days)

        word = list(words.keys())[j]

        print("-----> "+ word + " ?")
        answer = input("yes or no : ")

        if(answer == "yes"):
            numberOfYes += 1
        else:

            indexesFailed.append(j)


            p = subprocess.Popen(["python", "./openBrowser.py", word], shell=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL )

        
        if(i % clearThreshold == 0):
            os.system("clear")
            print("%.2f" % (i / numberOfWords * 100), "% of session is complete")
            print("left : ", numberOfWords - i)
            print("\n")

        print(word + ": ")
        print(words[word])
        
        print("\n\n\n")

    return indexesFailed



#main

while(1):

    randomIndexes = doSession(randomIndexes, words)
    randomIndexes = np.array(randomIndexes)
    np.random.shuffle(randomIndexes)

    answer = input(" \n  Do over? \n \n ")

    if(answer == "yes"):
        continue
    else:
        break

#endmain
















