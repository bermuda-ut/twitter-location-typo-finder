import re

NUMS = [str(a) for a in range(0,10)]
SUB = ['st', 'rd', 'nd', 'th']

def hasNum(s):
    for n in NUMS:
        if n in s:
            return True
    return False

def numProp(s):
    i = 0
    for n in NUMS:
        if n in s:
            i += 1
    return 1.0 * i / len(s)

def numCheck(s):
    for n in SUB:
        if n in s:
            return True
    if(numProp(s) < 0.8):
        return False
    return True


def loadDict(dictFp):
    l = set()

    for line in dictFp:
        line = re.sub("[^a-zA-Z 0-9\'\-,]", "", line)
        split = line.split()

        if(len(line) == 0):
            continue

        if(len(split) >= 2 and (split[1:] == ['Water', 'Well'] or split[1:] == ['Wtaer', 'Well'])):
            line = "Water Well"
        elif(len(split) >= 2 and split[1] == 'Reservoir'):
            line = "Reservoir"
        elif(len(split) >= 2 and split[1] == 'Well'):
            line = "Well"
        elif(len(split) >= 3 and split[2] == 'Well' and split[1] in ['C', 'M']):
            line = "Well"
        elif(len(split) >= 2 and split[1] == 'Spring'):
            line = 'Spring'

        split = line.split(' ')

        for word in split:
            if not len(word):
                continue

            #if word[0] in ["'", "-"]:
            #    word = word[1:]
            '''
            if(word.isnumeric() or\
              (word[0].isnumeric() and word[len(word)-1].isnumeric()) or\
              (hasNum(word) and not numCheck(word))):
            '''
            if(not word.isalpha()):
                continue

            l.add(word) # add splitted form

        #l.add(line) # and also whole form

    return l
