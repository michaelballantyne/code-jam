class Bot:
    def __init__(self):
        self.pos = 1

    def move_towards(self, dest):
        if dest > self.pos:
            self.pos += 1
        elif dest < self.pos:
            self.pos -= 1

class BotSim:
    def __init__(self, seq):
        self.seq = seq
        self.orange = Bot()
        self.blue = Bot()
        self.total = 0

    def result(self):
        while len(self.seq) > 0:
            self.total += 1
            first = self.seq[0]
            fbot = self.orange if first[1] == 'O' else self.blue
            for pair in self.seq[1:]:
                if pair[1] == first[1]:
                    continue
                else:
                    sbot = self.orange if pair[1] == 'O' else self.blue
                    sbot.move_towards(pair[0])
                    break
            if fbot.pos == first[0]:
                self.seq.pop(0)
            else:
                fbot.move_towards(first[0])
        return self.total
            
if __name__ == "__main__":
    input = open("in.txt")
    out = open("out.txt", "w")
    input.readline()
    case = 1
    for line in input:
        l = line.split()
        l.pop(0)
        l2 = [(int(k),i) for i,k in zip(l[0::2], l[1::2])]
        sim = BotSim(l2)
        out.write("Case #" + str(case) + ": " + str(sim.result()) + '\n')
        case += 1

    input.close()
    out.close()


