import sys;

cases = int(sys.stdin.readline())
for casenum in range(1, cases + 1):
    line = sys.stdin.readline()[:-1]
    
    value_map = {line[0]: 1}

    nextval = 0
    for i in range(1,len(line)):
        if nextval == 1:
            nextval += 1;
        if line[i] not in value_map:
            value_map[line[i]] = nextval
            nextval += 1
    
    base = max(value_map.values()) + 1
    
    result = 0
    placeval = base ** (len(line)-1)
    for char in line:
        result += placeval * value_map[char]
        placeval /= base


    print "Case #" + str(casenum) + ": " + str(result)
