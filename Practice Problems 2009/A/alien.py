def translate(number, source, target):
    reverse_num = num[::-1]

    base10 = 0

    for i in range(len(reverse_num)):
        base10 = base10 + (source.index(reverse_num[i]) * len(source)**(i))

    result = ""
    while base10:
         result = result + target[base10 % len(target)]
         base10 = base10 // len(target)

    return result[::-1]

input = open("A-large-practice.in.txt")
output = open("A-large.out.txt", 'w')

cases = int(input.readline())

for case_number in range(1, cases+1):
    line = input.readline().rstrip("\n").split(" ")
    num, source, target = line
    output.write("Case #" + str(case_number) + ": " + translate(num, source, target) + "\n")

input.close()
output.close()