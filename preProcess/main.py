#!/bin/python3

from dictManager import *
from relevantFinder import buildRelevant
from tweetProcessor import *
import sys

def main():
    if(len(sys.argv) < 3 or "-help" in sys.argv):
        print("Not enough command line arguements")
        print("Usage: python3 main.py <Dictionary> <Input>")
        print("In relavance of our project, dictionary would be geo-locations")
        print("and input would be the tweets")
        return 1;

    try:
        dictFp = open(sys.argv[1], 'r')
    except:
        print("Unable to open dictionary file")
        return 2;

    try:
        inputFp = open(sys.argv[2], 'r')
    except:
        print("Unable to open input file")
        return 3;

    while True:
        c = input("Command (type help for commands): ")

        if c == 'd':
            print("Loading Dictionary..")
            dictList = sorted(list(loadDict(dictFp)))
            print("Finished loading dictionary")
            print("Writing Clean Dictionary..")

            outputFp = open(sys.argv[1] + '-custom.txt', 'w')
            for word in dictList:
                outputFp.write(word + "\n")
            outputFp.close()

            print("Wrote {} words".format(len(dictList)))

            dictFp = open(sys.argv[1], 'r')

        elif c == 't':
            print("Building Relevance Set..")
            ls = buildRelevant()

            print("Processing Tweets..")
            #outputFp = open(sys.argv[2] + '-custom.txt', 'w')

            digTweets(inputFp, ls, sys.argv[2])

            #outputFp.close()

            inputFp = open(sys.argv[2], 'r')

        elif 'help' in c:
            print("Command List:")
            print(" > d to build dictionary")
            print(" > t to build tweets")
            print(" > q to exit")

        elif c == 'q':
            print("Exiting..")
            break

        else:
            print("Unknown command")

        print("")

    dictFp.close()
    inputFp.close()
    return 0

print("Exited with status {}".format(main()));
