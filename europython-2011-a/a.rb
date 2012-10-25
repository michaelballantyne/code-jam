#!/usr/bin/ruby

STDIN.readline
STDIN.read.split("\n").each_with_index do |line, i|
    country = line.strip
    case country[-1, 1]
    when "y"
        st = "is ruled by nobody."
    when "a", "e", "i", "o", "u"
        st = "is ruled by a queen."
    else
        st = "is ruled by a king."
    end
    puts "Case #" + (i + 1).to_s + ": " + country + " " + st
end
