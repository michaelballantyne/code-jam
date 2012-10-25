import sys
f = sys.stdin

cases = int(f.readline())

for casenum in range(cases):
    credit = int(f.readline())
    numitems = int(f.readline())
    values = [int(value) for value in f.readline().split()]

    map = {}
    for i in range(len(values)):
        map[values[i]] = i + 1

    for i in range(len(values)):
        firstvalue = values[i]
        firstpos = i + 1
        remainder = credit - firstvalue

        try:
            secondpos = map[remainder]
        except KeyError:
            continue

        if firstpos == secondpos:
            continue


        print 'Case #' + str(casenum + 1) + ": " + str(firstpos) + " " + str(secondpos)
        break

