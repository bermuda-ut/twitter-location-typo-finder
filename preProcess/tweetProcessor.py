from nltk.stem.wordnet import WordNetLemmatizer
from relevantFinder import isRelevant
from nltk.corpus import stopwords
from nltk.corpus import names
from nltk.corpus import words as nltkWords
from nltk import pos_tag
from nltk import word_tokenize
import re

OPTION = ['NNP', 'NN']
#RATIOMIN = 0.09
#RATIOMIN_URL = 0.9
RATIOMIN = 0.05
SCOREMIN = 0.42 # 35 42 65 90
RATIOMIN_URL = 0.5
NLIST = names.words()
WLIST = nltkWords.words()

def filterSentence(sent, option):
    ls = pos_tag(word_tokenize(sent))
    final = ""
    skipNext = False

    for (word, ty) in ls:
        if skipNext:
            skipNext = False
        elif word == "@":
            skipNext = True
        elif (ty in option and len(word) > 2 and word not in NLIST and word.lower() not in WLIST):
            if(word == word.upper()): #deal with all Caps
                word = word[0] + word[1:].lower()
            final += (word + " ")

    return final[:-1]

def digTweets(inputFp, ls, inputDir):
    rel = 0
    s = set(stopwords.words('english')) #stop words
    outputDir = inputDir + "-min{}.txt".format(str(SCOREMIN).split('.')[1])
    outputFp = open(outputDir, 'w')

    for line in inputFp:
        splitted = line.split('\t')
        if(len(splitted) == 4):
            userID, tweetID, line, date = splitted

            cleanLine = re.sub('[^a-zA-Z| ]', "", line).split(' ') # ONLY alphabets
            splitLine = line.split(' ') # words
            filtered = [x.lower() for x in cleanLine if x not in s] # ONLY Alphabets + no stopwords

            wdcnt, score, totcnt, ratio = 0, 0, 0, 0
            for word in filtered:
                p = WordNetLemmatizer().lemmatize(word,'v')
                # ignores nouns, all verbs into present tense
                
                delta = isRelevant(p, ls)
                if(delta):
                    score += delta
                    wdcnt += 1
                totcnt += 1

            if(wdcnt):
                score = score / wdcnt
                ratio = wdcnt / totcnt

            ratioMinimum = RATIOMIN_URL if ('http' in line.lower() or '.com' in line.lower()) else RATIOMIN

            if(score >= SCOREMIN and ratio >= ratioMinimum):
                line = filterSentence(line, OPTION)
                if(line):
                    outputFp.write(userID + '\t' + tweetID + '\t' + line + '\t' + date)
                    rel += 1

    outputFp.close()

    print("Finished Processing, found {} relevant".format(rel))
