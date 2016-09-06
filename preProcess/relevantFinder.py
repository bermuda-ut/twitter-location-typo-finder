from nltk.corpus import wordnet as wn
from itertools import product

def buildRelevant():
    highP = {'travel', 'located', 'at', 'towards', 'visit'}
    midP = {'where', 'place', 'city', 'town', 'village', 'go',\
            'to', 'location', 'holiday', 'from', 'in', 'where'}
    norP = []

    for mid in highP.union(midP):
        t = wn.synsets(mid)
        for f in t:
            q = [w.replace('_', ' ') for s in f.closure(lambda s:s.hyponyms()) for w in s.lemma_names()]
            norP += q

    norP = set(norP)

    return(highP, midP, norP)

def isRelevant(word, scorer):
    sc = 0
    curr = 1

    for wordSet in scorer:
        if word in wordSet:
            sc += curr

        curr -= 0.4

    return sc

'''
usage:
ls = buildRelevant()

word = 'went'
proc = WordNetLemmatizer().lemmatize(word,'v')
print(proc)
print(isRelevant(proc, ls))
'''
