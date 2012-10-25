from math import sqrt 

def f(x,y,n):
    dist = sqrt(x ** 2 + y ** 2)
    if n - 1 < dist and dist < n:
        return "X"
    else:
        return "O"

def print_board(n):
    for j in range(n-1, -1, -1):
	print str(" ".join([f(i,j,n) for i in range(n)]))

print_board(10)