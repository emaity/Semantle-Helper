import os
import tqdm

from pathlib import Path
from gensim.models import KeyedVectors

def toUsable(value):
    return round(100*(value), 2)

possibleAnswers = []
newPossibleAnswers = [] # two lists: one for larger, previous possibilities, and newOne for culled version of previous
iterationCount = 0      # for figuring out whether to compare with all possibilties or not

print("Please wait...")
model = KeyedVectors.load('wordVectors.kvmodel')


while True:
    print("Enter a word and its similarity (on separate lines):")
    userGuess = input()
    guessSimilarity = float(input())

    if iterationCount == 0: # if we haven't looped, compare similarity to all possible keys
        for key in tqdm.tqdm(model.index_to_key):
            if (toUsable(model.similarity(userGuess, key)) == guessSimilarity):
                possibleAnswers.append(key)
        iterationCount += 1
        print("Possibilities:")
        print(possibleAnswers)
        continue

    if newPossibleAnswers: # if newPossibleAnswers is not empty, then
        possibleAnswers = newPossibleAnswers # previous list is now = new list
        newPossibleAnswers = []              # new list set empty for next culling of old list

    # otherwise, compare only with the possibleAnswers list
    for key in tqdm.tqdm(possibleAnswers):
        if(toUsable(model.similarity(userGuess, key).item()) == guessSimilarity):
            newPossibleAnswers.append(key)
    
    print("Possibilities:")
    print(newPossibleAnswers)

    if len(newPossibleAnswers) == 1: 
        print("The answer is: ", newPossibleAnswers[0])
        break
    if len(possibleAnswers) == 1:
        print("The answer is: ", possibleAnswers[0])
        break
os.system("pause")