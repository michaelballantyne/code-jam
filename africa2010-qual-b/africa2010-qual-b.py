import sys

cases = int(sys.stdin.readline())

for casenum in range(1, cases + 1):
    words = sys.stdin.readline().split()
    words.reverse()
    print "Case #" + str(casenum) + ": " + ' '.join(words)
