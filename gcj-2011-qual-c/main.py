#!/usr/bin/env python

import sys

f = sys.stdin
o = sys.stdout

numCases = int(f.next())
for caseNum in range(1, numCases + 1):
    f.next()
    candy_values = [ int(x) for x in f.next().split() ]
    if reduce(lambda x, y: x ^ y, candy_values) != 0:
        result = "NO"
    else:
        candy_values.sort()
        result = str(sum(candy_values[1:]))
    o.write("Case #" + str(caseNum) + ": " + result + "\n")
