import fuzzy
import math
import sys

# Python 2
def main():
    dictFp = open(sys.argv[1], 'r')
    inputFp = open(sys.argv[2], 'r')
    soundex = fuzzy.Soundex(5)

    d = []
    #print("Dictionary Loading")
    for line in dictFp:
        d.append(line.strip())

    d = sorted(d)
    s = []

    for a in d:
        s.append(soundex(a))

    #print("Dictionary Loaded")

    done = set()

    for line in inputFp:
        uid, tid, tweet, date = line.split('\t')

        words = tweet.split()
        for word in words:
            if(word in done):
                continue
            done.add(word)
            sdex = soundex(word)

            output = []
            for i in range(len(s)):
                if(s[i] == sdex):
                    output.append(d[i])

            if(len(output)):
                sys.stdout.write("{}: ".format(word))
                i = 0
                for w in output:
                    if w != word:
                        sys.stdout.write(w + " ")
                    i+=1
                    if(i == 10):
                        break;
                print("")


main()
