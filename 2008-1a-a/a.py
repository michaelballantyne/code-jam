import sys
cases = int(sys.stdin.readline())

def vec(): return sorted([int(x) for x in sys.stdin.readline().split()])

for i in range(1, cases + 1):
    sys.stdin.readline()
    print("Case #" + str(i) + ": " + str(sum([x*y for x,y in zip(vec(),reversed(vec()))])))
