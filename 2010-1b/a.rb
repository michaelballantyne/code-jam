#!/usr/bin/ruby
cases = STDIN.readline.to_i

def create(existing, tocreate)
    if existing.include?(tocreate) || tocreate.length == 0
        return 0
    end

    existing.push(tocreate)
    parentpath = tocreate.split('/')[0...-1].join('/')
    return 1 + create(existing, parentpath)
end

cases.times do |i|
    numexisting, numtocreate = STDIN.readline.split.map(&:to_i)
    existing = STDIN.lines.take(numexisting).map(&:strip)
    tocreate = STDIN.lines.take(numtocreate).map(&:strip)
    total = 0
    tocreate.each do |item|
        total += create(existing, item)
    end
    printf("Case #%d: %d\n", i + 1, total)
end
