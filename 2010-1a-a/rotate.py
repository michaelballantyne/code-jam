import sys, re

def value(m, r, c):
    return m[r][c] if 0 <= r and r < len(m) and 0 <= c and c < len(m[0]) else '.'

def isWin(m, t, n):
    for r in range(len(m)):
        for c in range(len(m[r])):
            for (rn, cn) in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
                if isWinRecursive(m, t, r, c, rn, cn, n):
                    return True
    return False

def isWinRecursive(m, t, r, c, rn, cn, n):
    return n == 0 or (value(m, r, c) == t and isWinRecursive(m, t, r + rn, c + cn, rn, cn, n - 1))

t = int(sys.stdin.readline())
for casenum in range(1, t + 1):
    k, n = [int(x) for x in sys.stdin.readline().split()]
    m = []
    for rownum in range(k):
        row = re.sub(r'\.', '',sys.stdin.readline().strip())
        m.append(''.join(['.' for i in range(k - len(row))]) + row)

    bwin = isWin(m, "B", n)
    rwin = isWin(m, "R", n)

    if bwin and rwin:
        rval = 'Both'
    elif bwin:
        rval = 'Blue'
    elif rwin:
        rval = 'Red'
    else:
        rval = 'Neither'

    print "Case #" + str(casenum) + ": " + rval
