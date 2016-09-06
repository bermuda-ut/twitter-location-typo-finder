import ngram
import math
import sys
from collections import defaultdict

def main():
    dictFp = open(sys.argv[1], 'r')
    inputFp = open(sys.argv[2], 'r')

    customN = int(sys.argv[3])
    threshold = float(sys.argv[4])

    d = []
    #print("Dictionary Loading")
    for line in dictFp:
        d.append(line.strip())
    D = ngram.NGram(d, N=customN)
    #print("Dictionary Loaded")

    outputDict = defaultdict(list)

    counter = 0
    for line in inputFp:
        print("#{}\t{}".format(counter, line), file=sys.stderr, end="")
        try:
            uid, tid, tweet, d = line.split('\t')
        except:
            continue
        words = tweet.split()

        for word in words:
            if(len(word) < 4):
                continue

            res = D.search(word, threshold=threshold)

            valid = True
            for found, prob in res:
                #if(found != word):
                    #output.append(found)
                if(found == word):
                    valid = False
                    break

            if(len(res) and valid): #and len(output)):
                res = ""
                #for w in output:
                #    res += (w + " ")
                #res += ("\t" + tid)
                print("> Identified {} as typo".format(word), file=sys.stderr)
                outputDict[word].append(tid)

        counter += 1

    for (k, v) in outputDict.items():
        print("{}\t".format(k), end="")
        for tid in v:
            print(tid, end=" ")
        print("")


main()
