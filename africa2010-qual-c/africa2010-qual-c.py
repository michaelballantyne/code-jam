import sys

keymap = {'\n': ('', 0), ' ': ('0', 1), 'a': ('2', 1), 'c': ('2', 3), 'b': ('2', 2), 'e': ('3', 2), 'd': ('3', 1), 'g': ('4', 1), 'f': ('3', 3), 'i': ('4', 3), 'h': ('4', 2), 'k': ('5', 2), 'j': ('5', 1), 'm': ('6', 1), 'l': ('5', 3), 'o': ('6', 3), 'n': ('6', 2), 'q': ('7', 2), 'p': ('7', 1), 's': ('7', 4), 'r': ('7', 3), 'u': ('8', 2), 't': ('8', 1), 'w': ('9', 1), 'v': ('8', 3), 'y': ('9', 3), 'x': ('9', 2), 'z': ('9', 4)}

cases = int(sys.stdin.readline())

for casenum in range(1, cases + 1):
    line = sys.stdin.readline()

    result = ""

    lastnum = None
    for letter in line:
        entry = keymap[letter]
        if entry[0] == lastnum:
            result += " "
        result += (entry[0] * entry[1])
        lastnum = entry[0]

    print "Case #" + str(casenum) + ": " + result
