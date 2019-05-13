'''
Assignment 2 - Write a program to find frequency of each distinct word in a given text file ‘input.txt’. Your Output
should be stored in a different file named ‘output.txt’ in alphanumeric order. Each line should
contain the word and its frequency separated by a comma. (if numeric values are present in file
they should be at the start of output file). You can take any text file as your input file.
'''
import re

#frequency calculation function
def frequencyCalculation(inputFileName,outputFileName):
    inputFile = open(inputFileName,'r')
    fileContents = inputFile.read()
    inputFile.close()
    wordList = fileContents.split()
    uniqueWordList = set(wordList)
    convert = lambda text: int(text) if text.isdigit() else text
    alphanumKey = lambda key: [convert(c) for c in re.split('([0-9]+)', key.strip())]
    sortedWordList =  sorted(uniqueWordList, key = alphanumKey)
    frequencyCount = {i:0 for i in sortedWordList}
    for i in wordList:
        frequencyCount[i]+=1

    outputFile = open(outputFileName,'w+')
    for i in sortedWordList:
        outputFile.write(i+","+str(frequencyCount[i])+"\n")
    outputFile.close()

if __name__=='__main__':
    frequencyCalculation('input.txt','output.txt')
