def equal(l1, l2, r, m):
    return m if l1 == l2 else r

def ged(f, t, r=-1, d=-1, i=-1, m=1):
    lf, lt = len(f), len(t)
    A = []
    row = [0] * (lf + 1)
    A.append(row.copy())

    for j in range(1, lf + 1):
        A[0][j] = j * d

    for j in range(1, lt + 1):
        A.append(row.copy())
        A[j][0] = j * i

    for j in range(1, lt + 1):
        for k in range(1, lf + 1):
            A[j][k] = max(\
                    A[j][k-1] + d,\
                    A[j-1][k] + i,\
                    A[j-1][k-1] + equal(t[j-1], f[k-1], r, m))

    return(A[lt][lf])

def ngram(word, comp, n=2):
    wdls, compls = [], []

    wdls.append('#'+word[:n-1])
    compls.append('#'+comp[:n-1])

    for i in range(0, len(word)-n+1, 1):
        wdls.append(word[i:i+n])
    for i in range(0, len(comp)-n+1, 1):
        compls.append(comp[i:i+n])

    wdls.append(word[-(n-1):]+'#')
    compls.append(comp[-(n-1):]+'#')

    tot = len(compls) + len(wdls)
    i = 0
    for elem in wdls:
        if elem in compls:
            compls.remove(elem)
            i+=1

    dist = tot - i * 2

    return 1 - dist / tot
    
