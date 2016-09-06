import sys

def main():
    a = open(sys.argv[1], 'r')
    b = open(sys.argv[2], 'r')
    aset = set()
    bset = set()

    for line in a:
        word = line.split('\t')[0]
        aset.add(word)

    for line in b:
        word = line.split('\t')[0]
        bset.add(word)

    for word in aset:
        if word not in bset:
            print(word)

    return 0

main()
